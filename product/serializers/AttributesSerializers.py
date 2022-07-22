from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from product.models.attributes import Attribute, CategoryAttribute, ProductAttributeValues


class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'attribute_name', 'is_active']
        read_only_fields = ['id']


class CategoryAttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryAttribute
        fields = ['id', 'sub_category_id', 'attribute_id']
        read_only_fields = ['id']



class ProductAttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductAttributeValues
        fields  = ['id', 'product_inv_id', 'attribute_id', 'attribute_value']
        read_only_fields = ['id']
        