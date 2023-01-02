from rest_framework.serializers import ModelSerializer

from home.models.CountryModel import CountryModel


class CountrySerializer(ModelSerializer):

    class Meta:
        model = CountryModel
        fields  = ['id' , "iso" , "country_name" , "nice_name" , "iso_3" , "num_code" , "phone_code"]
        read_only_fields = ['id'] 