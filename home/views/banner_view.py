from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from home.serializers.BannerImageUploadSerializer import BannerImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser




class AddBannerImageView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser ]

    def post(self, request, format= None):
        print('data', request.data)
        serializer =  BannerImageSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                res = {'status': status.HTTP_400_BAD_REQUEST, 'error': f'{e}'}
                return Response(res,  status= status.HTTP_400_BAD_REQUEST)
            res = {'status': status.HTTP_200_OK, 'msg': 'Banner Image Added Successfully!!'}
            return Response(res)
            
        else:
            res =  {
                'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'errors': serializer.errors
            }
            return Response(res, status= status.HTTP_400_BAD_REQUEST)


