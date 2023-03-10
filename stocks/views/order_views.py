from django.db import connection
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from product.custompermissions import AdminCanAdd
from stocks.serializers.OrderSerializers import CartOderSerializer, SingleProductOrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


# view to add full product including images and items and attribute(a complete product)
class PlaceOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, format = None):
        request_data = dict(request.data) 
        order_type  =   request_data.pop('order_type')

        if order_type  == 'only-product-checkout':
            request_data.get('order')['ordered_by'] =  request.user.id
            serializer  =  SingleProductOrderSerializer(data = request_data )
        elif order_type == 'cart-checkout':
            request_data['ordered_by'] =  request.user.id
            print('requrest data', request_data)
            serializer  =  CartOderSerializer(data =  request_data, context={'request': request} )
        else:
            res =  {
                'status': status.HTTP_400_BAD_REQUEST, 
                'msg': 'Checkout Type not Specified or Not allowed!!!'
            }
            return  Response(res, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
                return Response(res,  status= status.HTTP_400_BAD_REQUEST)
            res = {'status': status.HTTP_200_OK, 'msg': 'Order Placed Successfully!!'}
            return Response(res)
            
        else:
            res =  {
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)
            






class ShowAllOrdersView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, AdminCanAdd]

    def get(self, request):
        try:
            id  = int(request.GET['id'])
        except :
            id =  0 

        with connection.cursor() as cursor:
            if id == 0:
                cursor.execute("SELECT * FROM inventory.order_view  WHERE delivered_date IS NULL ORDER BY  id DESC")
            else:
                cursor.execute("SELECT * FROM inventory.order_view  WHERE delivered_date IS NULL AND ID = %s", [id])
            
            row  =  [dict(zip([column[0] for column in cursor.description], row))
                    for row in cursor.fetchall()]
                    

            res  =  {'status':status.HTTP_200_OK, 'results':row }
            return JsonResponse(res, safe=False)