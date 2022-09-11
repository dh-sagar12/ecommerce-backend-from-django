from ast import Delete
from urllib import request
from rest_framework.views import APIView
from rest_framework.permissions import  IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from product.custompermissions import AdminCanAdd
from product.models.Images import Images
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
    

    def delete(self, request):
        id =  request.data.get('id')
        try:
            imag_instance =  Images.objects.get(id=id)
        except Exception as e:
            res = {'error': f'{e}', 'status': status.HTTP_404_NOT_FOUND }
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        try:
            imag_instance.delete()
            return Response({'msg': f'Image has been deleted successfully!!', 'status': status.HTTP_200_OK})
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    
