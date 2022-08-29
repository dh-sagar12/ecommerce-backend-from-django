from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from product.models.attributes import Attribute, CategoryAttribute, ProductAttributeValues



# serialzer used to do operation on attribute name like (size, Height, Width etc )
class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'attribute_name', 'is_active']
        read_only_fields = ['id']



# used to mapp serialzer name with sub cateogry id so that if one sub category choosed then only atttribute of that cateogry to be fetched in front end 
class CategoryAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryAttribute
        fields = ['id', 'sub_category_id', 'attribute_id']
        read_only_fields = ['id']


# serialzer use to save atttribute and theier value to the table accorridnly 
class ProductAttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAttributeValues
        fields  = ['id', 'product_inv_id', 'attribute_id', 'attribute_value']
        read_only_fields = ['id']
        