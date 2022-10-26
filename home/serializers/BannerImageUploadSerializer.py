from rest_framework.serializers import ModelSerializer

from home.models.BannerModel import BannerPicture


class BannerImageSerializer(ModelSerializer):
    class Meta:
        model = BannerPicture
        fields  = ['id', 'alt_text', 'redirect_url', 'is_active', 'file_name', 'created_on']
        read_only_fields = ['id', 'created_on']