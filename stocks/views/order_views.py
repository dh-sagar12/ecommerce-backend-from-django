from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from stocks.serializers.OrderSerializers import CartOderSerializer, SingleProductOrderSerializer
from rest_framework.response import Response
from rest_framework import status




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
            
