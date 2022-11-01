
from product.custompermissions import AdminCanAdd
from product.serializers.AttributesSerializers import AttributeSerializer, CategoryAttributeSerializer, ProductAttributeValueSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from product.models.attributes import Attribute, CategoryAttribute, ProductAttributeValues
from django.db import connection
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView


class AttributeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def  post(self, request, format= None):
        serializer =  AttributeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {'msg': 'Data Saved successfully!!'}
            return Response(res)
        except Exception as e:
            res =  {'error': f'{e}'}
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)


    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            attribute_instance = Attribute.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = AttributeSerializer(attribute_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Attribute has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



class GetAttributeView(APIView):
    pagination_class = PageNumberPagination
    def get(self, request):
        items = Attribute.objects.filter(is_active =  True)
        serializer = AttributeSerializer(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)



    

class CategoryAttributeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def  post(self, request, format= None):
        serializer =  CategoryAttributeSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {'msg': 'Data Saved successfully!!'}
            return Response(res)
        except Exception as e:
            res =  {'error': f'{e}'}
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)


    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            category_attribute_instance = CategoryAttribute.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = CategoryAttributeSerializer(category_attribute_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Attribute has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class GetCategoryAttributeView(APIView):
    def get(self, request):
        items = CategoryAttribute.objects.all()
        serializer = CategoryAttributeSerializer(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)



    
class ProductAttributeValueView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, AdminCanAdd]
    def  post(self, request, format= None):
        serializer =  ProductAttributeValueSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {'msg': 'Data Saved successfully!!'}
            return Response(res)
        except Exception as e:
            res =  {'error': f'{e}'}
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)


    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            product_attribute_value_instance = ProductAttributeValues.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductAttributeValueSerializer(product_attribute_value_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Attribute value has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        id =  request.data.get('id')
        try:
            product_att_val_instance =  ProductAttributeValues.objects.get(id=id)
        except Exception as e:
            res = {'error': f'{e}', 'status': status.HTTP_404_NOT_FOUND }
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        try:
            product_att_val_instance.delete()
            return Response({'msg': f'Attribute has been deleted successfully!!', 'status': status.HTTP_200_OK})
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)



    
class GetProductAttributeValueView(APIView):
    def get(self, request):
        items = ProductAttributeValues.objects.all()
        serializer = ProductAttributeValueSerializer(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)




def get_attribute_value_with_item_id(request):
    if request.method == 'GET':
        product_item_id = request.GET.get('product_item_id')
        cursor  = connection.cursor()
        cursor.callproc('product.get_attribute_value_by_product_item_id', [product_item_id ])
        result =  [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
        return JsonResponse(result, safe=False)
    else:
        result  =  {
            "error": status.HTTP_400_BAD_REQUEST,
            "msg": 'Method Not Allowed'
        }
        return JsonResponse(result, safe=False)

        


