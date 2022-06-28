
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
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            category_instance = Category.objects.get(id=id)
            print(category_instance)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Category has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        id =  request.data.get('id')
        try:
            category_instance =  Category.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        try:
            category_instance.delete()
            return Response({'msg': f'{category_instance.name} has been deleted successfully!!'})
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

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


class UpdateDeleteSubCategory(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]
    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            sub_category_instance = SubCategory.objects.get(id=id)
            print(sub_category_instance)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = SubCategorySerializer(sub_category_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Sub Category has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        id =  request.data.get('id')
        try:
            sub_category_instance =  SubCategory.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        try:
            sub_category_instance.delete()
            return Response({'msg': f'{sub_category_instance.name} has been deleted successfully!!'})
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)