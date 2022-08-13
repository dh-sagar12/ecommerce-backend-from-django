from urllib import request
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from product.custompermissions import AdminCanAdd
from product.serializers.ImageSerializer import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser



class AddImages(APIView):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AdminCanAdd]
    parser_classes = [MultiPartParser, FormParser, JSONParser ]
    def  post(self, request, format= None):
        serializer =  ImageSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        res = {'msg': 'Data Saved successfully!!'}
        return Response(res)

    
