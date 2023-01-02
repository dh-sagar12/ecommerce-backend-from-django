from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from account.models.user import GenderModel
from account.models.user import User
from account.serializers.AuthenticationSerializers import GetGenderSerializer, UserLoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView  


# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }



class UserCreationView(APIView):
  
  def post(self, request, format = None):

    serializer  =  UserSerializer(data =  request.data)
    if serializer.is_valid():
      try:
        serializer.save()
        res =  {
          'status': status.HTTP_200_OK, 'msg': 'User registration succeed!!!'
        }
        return Response(res, status=status.HTTP_200_OK)

      except Exception as e:
        print('exception', e)
        res = {
          'error': f'{e}', 
          'status': status.HTTP_400_BAD_REQUEST
        }
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
    else:
      res  ={
        'status': status.HTTP_400_BAD_REQUEST,
        'errors': serializer.errors
      }
      return Response(res, status=status.HTTP_400_BAD_REQUEST)



# Create your views here.
class UserLoginView(APIView):
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    password = serializer.data.get('password')
    user = authenticate(email=email, password=password)
    if user is not None:
      token = get_tokens_for_user(user)
      # Response.set_cookie('gusty_auth_token', token['refresh'],  max_age=3600 * 24 * 365 * 2)
      return Response({'token':token, 'msg':f'Welcome {user.first_name}'}, status=status.HTTP_200_OK)
      # return Response
    else:
      return Response({'errors':'Email or Password is not Valid'}, status=401, content_type='application/json')



class GetUserData(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self, request):
    serializer =  UserSerializer(request.user )
    return Response({'status': status.HTTP_200_OK, 'data':serializer.data}, status=status.HTTP_200_OK)    



class GetGenderData(ListAPIView):
    queryset = GenderModel.objects.all().order_by('id')
    serializer_class = GetGenderSerializer
