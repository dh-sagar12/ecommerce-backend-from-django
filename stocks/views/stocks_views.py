from django.db import connection
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from stocks.serializers.StockSerializers import ProductItemStockSerializer


class AddStockView(APIView):

    def post(self, request):
        serializer  =  ProductItemStockSerializer(data =  request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
                return Response(res,  status= status.HTTP_400_BAD_REQUEST)
            res = {'status': status.HTTP_200_OK, 'msg': 'Stock Added Successfully!!'}
            return Response(res)
            
        else:
            res =  {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)



def get_stock_qty_of_product_item(request):
    if request.method == 'GET':
        product_item_id = request.GET.get('product_item_id')
        cursor  = connection.cursor()
        cursor.callproc('inventory.get_stock_qty_of_product_item', [product_item_id ])
        result =  [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
        return JsonResponse(result, safe=False)


