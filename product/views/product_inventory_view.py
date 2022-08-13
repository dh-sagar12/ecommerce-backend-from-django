from email.mime import image
from product.custompermissions import AdminCanAdd
from product.models.Images import Images
from product.models.productInventory import ProductInventory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import transaction

from product.serializers.ProductInventorySerializer import ProductInventorySerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser



class AddNewProductInventory(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, AdminCanAdd]
    parser_classes = [MultiPartParser, FormParser, JSONParser ]

    def post(self, request, format= None):
        print(request.data)
        serializer =  ProductInventorySerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                res = {'status': status.HTTP_200_OK,  'success': 'Data Saved successfully!!'}
                return Response(res)
            except Exception as e:
                res =  {'error': f'{e}'}
                return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            res = {
                'status': status.HTTP_400_BAD_REQUEST,
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)

class GetProductInventory(APIView):
    def get(self, request):
        items = ProductInventory.objects.all()
        serializer = ProductInventorySerializer(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)



class UpdateDeleteProductInventory(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            product_inv_instance = ProductInventory.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductInventorySerializer(product_inv_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Product Inventory has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)