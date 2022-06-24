from rest_framework import serializers
from product.models.category import Category
from product.models.product import Product



class ProductSerializer(serializers.ModelSerializer):
    # id = serializers.PrimaryKeyRelatedField(read_only =True)
    # name= serializers.CharField(max_length=150)
    # description =  serializers.CharField(max_length=1000 )
    # slug = serializers.SlugField(read_only=True)
    # category_id = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all())
    # is_active = serializers.BooleanField(default=True)
    # created_on  = serializers.DateTimeField(read_only= True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'slug', 'category_id', 'sub_category_id', 'is_active', "created_on"]
        read_only_fields = ['id', 'slug', 'created_on']
        # extra_kwargs = {'name': {'read_only: True'}} another method to do 


    # THIS IS HOW WE  DO VALIDATION
    # def validate_name(self, value):
    #     if len(value) > 10:
    #         raise serializers.ValidationError('Name Must be Less an 10 characters')
    #     return value
