from rest_framework import serializers
from product.models.category import Category, SubCategory
from product.models.product import Product



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug',  'is_active', "created_on"]
        read_only_fields = ['id', 'slug', 'created_on']

    
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name', 'slug', 'category_id', 'is_active', "created_on"]
        read_only_fields = ['id', 'slug', 'created_on']