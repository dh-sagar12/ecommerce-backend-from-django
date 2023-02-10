from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from account.models.user import GenderModel, ShippingDetailMOdel
from account.models.user import User
from account.serializers.AuthenticationSerializers import GetGenderSerializer, UserLoginSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView

from account.serializers.UserDetailsSerializer import ShippingDetailSerializer  


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
    print(user)
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





class UserShippingDetailView(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes  =  [IsAuthenticated]
  def get(self, request):
    shipping_datail  =  ShippingDetailMOdel.objects.filter(user_id = request.user.id)
    serializer  =  ShippingDetailSerializer(shipping_datail, many= True)
    return Response({'status': 200, 'data': serializer.data}, status=status.HTTP_200_OK)


  def post(self, request):
        request_data = dict(request.data)
        request_data["user_id"] = request.user.id
        serializer  =  ShippingDetailSerializer(data = request_data, context={'request': request} )
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
                return Response(res,  status= status.HTTP_400_BAD_REQUEST) 
            res = {
                'status': status.HTTP_200_OK, 
                'msg': 'Shipping details added'
                }
            return Response(res)
            
        else:
            res =  {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)



  def put(self, request, format=None):
        id = request.data.get('id')
        try:
            shipping_detail_instance = ShippingDetailMOdel.objects.get(id=id, user_id  =  request.user.id)
        except Exception as e:
            res = {'status': status.HTTP_404_NOT_FOUND, 'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = ShippingDetailSerializer(shipping_detail_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK,  "msg": 'Shipped details has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)    
    
  def delete(self, request):
      id = request.data.get('id')
      try:
          shipping_detail_instance = ShippingDetailMOdel.objects.get(id=id)
      except Exception as e:
          res = {'error': f'{e}', "cart_id": id}
          return Response(res, status= status.HTTP_404_NOT_FOUND)
      try:
          shipping_detail_instance.delete()
          return Response({'msg': f'Shipping details has been deleted successfully!!', 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
      except Exception as e:
          res = {'error': f'{e}'}
          return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetGenderData(ListAPIView):
    queryset = GenderModel.objects.all().order_by('id')
    serializer_class = GetGenderSerializer
