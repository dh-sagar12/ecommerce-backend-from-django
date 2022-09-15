from email.mime import image
from functools import partial
import json
from product.custompermissions import AdminCanAdd
from product.models.Images import Images
from product.models.productInventory import ProductInventory
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from rest_framework.decorators import api_view
from django.db.models import Prefetch

from product.serializers.ProductInventorySerializer import ProductInventorySerializer, ProductInventorySerializerForGetMethod
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


 
# add product item + images and attributes in together 
class AddNewProductInventory(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, AdminCanAdd]
    parser_classes = [MultiPartParser, FormParser, JSONParser ]

    def post(self, request, format= None):
        print('data', request.data)
        serializer =  ProductInventorySerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                res = {'status': status.HTTP_200_OK,  'msg': 'Data Saved successfully!!'}
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



#TO get all the product inventory in the database(all means of all product)
class GetProductInventory(APIView):
    def get(self, request):
        items = ProductInventory.objects.prefetch_related(
    Prefetch('images', queryset=Images.objects.filter(is_active=True), to_attr='image_list')
    )
        serializer = ProductInventorySerializerForGetMethod(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)




# to view on product item and its images and attributes (get method)
@api_view(['GET'])
def view_product_items_view(request, pk):
    if request.method == 'GET':
        try:
            product_item = ProductInventory.objects.prefetch_related(
    Prefetch('images', queryset=Images.objects.filter(is_active=True), to_attr='image_list')
    ).get(id=pk)
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res)
        serializer =  ProductInventorySerializerForGetMethod(product_item)
        return Response(serializer.data)
    else:
        return Response({'msg':'request method not allowed'}, status= status.HTTP_400_BAD_REQUEST)




# update and delete in product items  which included image and attribute also
class UpdateDeleteProductInventory(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, AdminCanAdd]
    parser_classes = [MultiPartParser, FormParser, JSONParser ]
    def put(self, request):
        product_item = request.data.get('product_item')
        product_item_load = json.loads(product_item)
        serializer = ProductInventorySerializer(product_item_load, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK, "msg": 'Product Inventory has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)