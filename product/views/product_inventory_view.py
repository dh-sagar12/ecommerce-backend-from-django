from urllib import response
from product import serializers
from product.custompermissions import AdminCanAdd
from product.models.category import Category, SubCategory
from product.models.productInventory import ProductInventory
from product.serializers.CategorySerializer import CategorySerializer, SubCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from product.serializers.ProductInventorySerializer import ProductInventorySerializer



class AddNewProductInventory(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def post(self, request, format= None):
        serializer =  ProductInventorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {'msg': 'Data Saved successfully!!'}
            return Response(res)
        except Exception as e:
            res =  {'error': f'{e}'}
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)


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