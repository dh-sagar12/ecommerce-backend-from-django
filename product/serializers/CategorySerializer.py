from rest_framework import serializers
from product.models.category import Category, SubCategory
from product.models.product import Product



# serializer to create and view sub cateogory 
class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name', 'slug', 'category_id', 'is_active', "created_on"]
        read_only_fields = ['id', 'slug', 'created_on']


# serializer to create and view  cateogory 
class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many= True, read_only =  True)
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'slug',  'is_active', 'thumbnail_img' , 'description', 'sub_categories', "created_on"]
        read_only_fields = ['id', 'slug', 'sub_categories', 'created_on']