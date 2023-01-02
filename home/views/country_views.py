from rest_framework.views import APIView
from home.models.CountryModel import CountryModel
from home.serializers.CountrySerializer import CountrySerializer
from rest_framework.response import Response



class CountryView(APIView):
    def get(self, request):
        banners  =  CountryModel.objects.all().order_by('id')
        serializer =  CountrySerializer(banners, many =  True)
        return Response(serializer.data)
 