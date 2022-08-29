# from ..serializers.ProductInventorySerializer import FullProductWithInventorySerializer
from tkinter import EXCEPTION
from ..models.brands import Brands
from product.models.product import Product
from product.serializers.productSerializer import BrandSerializer, FullProductWithInventorySerializer, ProductSerializerForGetMethod, ProductOnlySerializer, ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class GetFullProductView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        product = Product.objects.all()
        serializer =  ProductSerializerForGetMethod(product,  many = True )
        return Response(serializer.data)



# to view all the product only with one extra item i.e. one images 
# it is joing product table with image table but not include product_inventory table and attribute table
class GetOnlyProductView(APIView):
    def get(self, request):
        product =  Product.objects.all()
        serializer  = ProductOnlySerializer(product, many= True)
        return Response(serializer.data)
        

class GetOneSingleProductView(APIView):
    def get(self, request, pk):
        try:
            product =  Product.objects.get(id=pk)
        except Exception as e:
            res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
            return Response(res)
        serializer =  ProductOnlySerializer(product)
        return Response(serializer.data)




# view to view one product by passing pk in URl including (product image, atrribute and all the dependencies table )
@api_view(['GET'])
def view_product_view(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id = pk)
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res)
        serializer =  ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response({'msg':'request method not allowed'}, status= status.HTTP_400_BAD_REQUEST)




# view to create only product not its images and items 
class AddNewProduct(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def  post(self, request, format= None):
        serializer =  ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        res = {'msg': 'Data Saved successfully!!'}
        return Response(res)


# view to add full product including images and items and attribute(a complete product)
class AddFullProduct(APIView):
    def post(self, request, format = None):
        serializer = FullProductWithInventorySerializer(data= request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
                return Response(res,  status= status.HTTP_400_BAD_REQUEST)
            res = {'status': status.HTTP_200_OK, 'msg': 'Product Created Successfully!!'}
            return Response(res)
            
        else:
            res =  {
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)
            
 



class UpdateDeleteProduct(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            product_instance = Product.objects.get(id=id)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": 'Product has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        id = request.data.get('id')
        try:
            product_instance = Product.objects.get(id=id)
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_404_NOT_FOUND)
        try:
            product_instance.delete()
            return Response({'msg': f'Product {product_instance.name} has been deleted successfully!!'})
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)



# view to fetch all the data in brand table 
class GetBrandsView(APIView):
    def get(self, request):
        brands = Brands.objects.all()
        serializer =  BrandSerializer(brands, many = True)
        return Response(serializer.data)