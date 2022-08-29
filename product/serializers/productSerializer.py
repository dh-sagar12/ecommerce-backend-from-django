from dataclasses import fields
from itertools import product
import json
from pyexpat import model
from rest_framework import serializers
from product.models.Images import Images
from product.serializers.AttributesSerializers import ProductAttributeValueSerializer
from django.db import transaction
from product.serializers.ImageSerializer import ImageSerializer
from product.serializers.ProductInventorySerializer import ProductInventorySerializer, SingleProductItemSerializer
from ..models.brands import Brands
from product.models.product import Product



# to create only a product not items and inventory(it is futher using in FullProductWithInventorySerializer
# serializer to create full product including all its attributes and images
class ProductSerializer(serializers.ModelSerializer):
    product_items =  ProductInventorySerializer(read_only = True, many= True)
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'slug', 'category_id', 'sub_category_id', 'brand_id', 'is_active',  "created_on", 'product_items' ]
        read_only_fields = ['id', 'slug', 'created_on', 'product_items']



# to view all the product with items, image atrribute and all 
class ProductSerializerForGetMethod(ProductSerializer):
    class Meta(ProductSerializer.Meta):
        model = Product
        fields =  ProductSerializer.Meta.fields
        read_only_fields =  ProductSerializer.Meta.read_only_fields
        depth = 1


    

# to view only one product and images not product item and their atrribute 
class ProductOnlySerializer(serializers.ModelSerializer):
    image =  ImageSerializer(read_only=True, many=True)
    class Meta:
        model =  Product
        fields= '__all__'
        read_only_fields = ['id', 'slug', 'image', 'created_on',]
        depth =1



# to create full product with all the required attribute, images and all 
class FullProductWithInventorySerializer(serializers.ModelSerializer):
    product  =  serializers.JSONField()
    product_item =  serializers.JSONField()
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = True),
        write_only = True
    )
    attributes_value =  serializers.ListField(
        child =  serializers.JSONField(),
        write_only =  True, 
    )

    class Meta():
        model = Product
        fields =  ['product', 'product_item',  'uploaded_images', 'attributes_value']



    @transaction.atomic
    def create(self, validated_data):
        product_data =  validated_data.pop('product')
        product_item_data =  validated_data.pop('product_item')
        uploaded_images = validated_data.pop('uploaded_images')
        attributes_value =  validated_data.pop('attributes_value')
        productInstance  =  ProductSerializer(data = product_data)
        productInstance.is_valid(raise_exception=True)
        product_return = productInstance.save()
        product_item_data.update({'product_id': product_return.id})
        new_product_inventory = SingleProductItemSerializer(data =  product_item_data)
        new_product_inventory.is_valid(raise_exception=True)
        productItemInstance =  new_product_inventory.save()
        
        for uploaded_item in uploaded_images:
            Images.objects.create(product_inventory_id = productItemInstance, product_id = product_return,  file_name = uploaded_item)

        for attr_value in attributes_value:
            dict_attribute = json.loads(attr_value)
            dict_attribute.update({"product_inv_id": productItemInstance.id})
            serializer = ProductAttributeValueSerializer(data = dict_attribute)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return productInstance

       



# serialzer to view all the brand information in brand table 
class BrandSerializer(serializers.ModelSerializer):    
    class Meta:
        model =  Brands
        fields = ['id', 'brand_name', 'description', 'is_active',]
        read_only_fields = ['id', 'created_on']
    

