
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from stocks.models.CartModels import CartModel
from stocks.serializers.CartSerializers import UserCartSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import connection



class UserCartView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        request_data = dict(request.data)
        request_data["user_id"] = request.user.id
        serializer  =  UserCartSerializer(data = request_data, context={'request': request} )
        if serializer.is_valid():
            try:
                serializer.save()
                response_data  =  self.get(request=request)
                # added_data =  response_data.content.decode('utf-8')
                added_data =  json.loads(response_data.content.decode('utf-8'))
                added_data =  added_data['results']
            except Exception as e:
                res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
                return Response(res,  status= status.HTTP_400_BAD_REQUEST) 
            res = {
                'status': status.HTTP_200_OK, 
                'msg': 'Added to cart!!',
                'added_data': added_data
                }

            return Response(res)
            
        else:
            res =  {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            id  = self.request.data['id']
        except :
            id =  0 

        with connection.cursor() as cursor:
            if id == 0:
                cursor.execute("SELECT * FROM inventory.cart_view WHERE user_id  =%s AND status AND  order_id IS NULL", [request.user.id])
            else:
                cursor.execute("SELECT * FROM inventory.cart_view WHERE  id= %s  AND  user_id  =%s AND status AND  order_id IS NULL", [id, request.user.id])
            
            row  =  [dict(zip([column[0] for column in cursor.description], row))
                    for row in cursor.fetchall()]
                    

            res  =  {'status':status.HTTP_200_OK, 'results':row }
            return JsonResponse(res, safe=False)

    def put(self, request, format=None):
        id = request.data.get('id')
        try:
            cart_instance = CartModel.objects.get(id=id)
        except Exception as e:
            res = {'status': status.HTTP_404_NOT_FOUND, 'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = UserCartSerializer(cart_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK,  "msg": 'Cart has been updated sucessfully!!'})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request):
        id = request.data.get('id')
        print(id)
        try:
            cart_instance = CartModel.objects.get(id=id)
        except Exception as e:
            res = {'error': f'{e}', "cart_id": id}
            return Response(res, status= status.HTTP_404_NOT_FOUND)
        try:
            cart_instance.delete()
            return Response({'msg': f'Cart has been deleted successfully!!', 'status': status.HTTP_200_OK}, status=status.HTTP_200_OK)
        except Exception as e:
            res = {'error': f'{e}'}
            return Response(res, status= status.HTTP_500_INTERNAL_SERVER_ERROR)