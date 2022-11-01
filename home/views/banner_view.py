from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from home.models.BannerModel import BannerPicture

from home.serializers.BannerImageUploadSerializer import BannerImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser




class AddBannerImageView(APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser ]

    def post(self, request, format= None):
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



class GetAllBannerImagesView(APIView):

    def get(self, request):
        active_only  =  request.GET['active_only']
        print('data is  ', active_only)
        if active_only == 'false':
            banners  =  BannerPicture.objects.all().order_by('-is_active')
        else:
            banners =  BannerPicture.objects.filter(is_active=  True)
        serializer =  BannerImageSerializer(banners, many =  True)
        return Response(serializer.data)
    

class UpdateBannerImages(APIView):
    def put(self, request):
        id = request.data.get('id')
        try:
            is_active =  request.data.get('is_active')
            banner_status = 'Active' if is_active == True else 'InActive'
        except Exception as e:
            res = {'status': status.HTTP_404_NOT_FOUND, 'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)

        try:
            product_instance = BannerPicture.objects.get(id=id)
        except Exception as e:
            res = {'status': status.HTTP_404_NOT_FOUND, 'msg': f'{e}'}
            return Response(res, status=status.HTTP_404_NOT_FOUND)
        serializer = BannerImageSerializer(product_instance, data= request.data, partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": status.HTTP_200_OK,  "msg": f'Banner Image set to {banner_status} '})
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)