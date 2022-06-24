from urllib import response
from product import serializers
from product.custompermissions import AdminCanAdd
from product.models.category import Category, SubCategory
from product.serializers.CategorySerializer import CategorySerializer, SubCategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class AddNewCategory(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def  post(self, request, format= None):
        serializer =  CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {'msg': 'Data Saved successfully!!'}
            return Response(res)
        except Exception as e:
            res =  {'error': f'{e}'}
            return Response(res, status=status.HTTP_406_NOT_ACCEPTABLE)


class GetCategory(APIView):
    def get(self, request):
        items = Category.objects.all()
        serializer = CategorySerializer(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)

class UpdateDeleteCategory(APIView):
    pass


class AddNewSubCategory(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def  post(self, request, format= None):
        serializer =  SubCategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            res = {'msg': 'Data Saved successfully!!'}
            return Response(res)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response( res, status=status.HTTP_406_NOT_ACCEPTABLE)


class GetSubCategory(APIView):
    def get(self, request):
        items = SubCategory.objects.all()
        serializer = SubCategorySerializer(items, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)