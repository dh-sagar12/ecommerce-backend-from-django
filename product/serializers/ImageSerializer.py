
from rest_framework import serializers
from product.models.Images import Images


# serializers to be used to do operation on image table 
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['id', 'product_inventory_id', 'product_id', 'file_name', 'created_on']
        read_only_fields = ['id', 'created_on']


    


    