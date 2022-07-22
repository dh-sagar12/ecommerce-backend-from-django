from product.models.product import Product
from product.serializers.productSerializer import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class GetProductView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        product = Product.objects.all()
        serializer =  ProductSerializer(product, many = True)
        return Response(serializer.data)


@api_view(['GET'])
def view_product_view(request, pk):
    if request.method == 'GET':
        try:
            product = Product.objects.get(id = pk)
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res)
        serializer =  ProductSerializer(product)
        return Response(serializer.data)
    else:
        return Response({'msg':'request method not allowed'}, status= status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
class AddNewProduct(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def  post(self, request, format= None):
        serializer =  ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as e:
            res = {'msg': f'{e}'}
            return Response(res, status=status.HTTP_400_BAD_REQUEST)
        res = {'msg': 'Data Saved successfully!!'}
        return Response(res)


# another way to do same thing as above
    # if request.method == 'POST':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     serializer = ProductSerializer(data = python_data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg': 'Data saved Successfully!!'}
    #         res_json_data = JSONRenderer().render(res)
    #         return HttpResponse(res_json_data, content_type='application/json')
    #     else:
    #         res_json_data =  JSONRenderer().render(serializer.errors)
    #         return HttpResponse(res_json_data, content_type='application/json')
    # else:
    #     return HttpResponseBadRequest('403 Forbidden!!'.format(request.method), status=403)


class UpdateDeleteProduct(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
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
