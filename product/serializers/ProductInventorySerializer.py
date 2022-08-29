from base64 import encode
import base64
from dataclasses import fields
import json
from pyexpat import model
from rest_framework import serializers
from product.models.Images import Images
from ..models.product import Product
from product.models.productInventory import ProductInventory
from product.serializers.AttributesSerializers import ProductAttributeValueSerializer
from product.serializers.ImageSerializer import ImageSerializer
from django.db import transaction

# from .productSerializer import ProductSerializer


# serialzer to used only to add  product items but not attribute and images  
class SingleProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductInventory
        fields = ['id', 'sku', 'product_id',  'is_active', 'is_default', 'store_price', 'discount', 'retail_price','created_on', 'updated_on' ]
        read_only_fields = ['id', 'sku', 'created_on',  'updated_on' ]
        







# serializers to be used to create product items including images and attribute but not create product itself. it is basicaly used to add items inside a product 
class ProductInventorySerializer(serializers.ModelSerializer):
    images  =  ImageSerializer(many=True, read_only=  True)
    attributes =  ProductAttributeValueSerializer(many=  True, read_only =  True)
    
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = True),
        write_only = True
    )

    attributes_value =  serializers.ListField(
        child =  serializers.JSONField(),
        write_only =  True, 
    )
    
    class Meta:
        model = ProductInventory
        fields = ['id', 'sku', 'product_id',  'is_active', 'is_default', 'store_price', 'discount', 'retail_price', 'images', 'uploaded_images', 'attributes', 'attributes_value', 'created_on', 'updated_on' ]
        read_only_fields = ['id', 'sku', 'created_on', 'images' , 'updated_on' ', attributes']

    @transaction.atomic
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        attributes_value =  validated_data.pop('attributes_value')
        print('attributes_value is', attributes_value)
        new_product_inventory = ProductInventory.objects.create(**validated_data)
        for uploaded_item in uploaded_images:
            new_product_image = Images.objects.create(product_inventory_id = new_product_inventory, file_name = uploaded_item)
        
        for attr_value in attributes_value:
            dict_attribute = json.loads(attr_value)
            dict_attribute.update({"product_inv_id": new_product_inventory.id})
            serializer = ProductAttributeValueSerializer(data = dict_attribute)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return new_product_inventory



# class FullProductWithInventorySerializer(ProductInventorySerializer):
#     product  =  serializers.JSONField()

#     class Meta(ProductInventorySerializer.Meta):
#         fields = ProductInventorySerializer.Meta.fields + ['product']
#         fields.remove('product_id')


#     @transaction.atomic
#     def create(self, validated_data):
#         uploaded_images = validated_data.pop('uploaded_images')
#         attributes_value =  validated_data.pop('attributes_value')
#         product_data =  validated_data.pop('product')
#         print('product_data: ', product_data, type(product_data))
#         # productInstance =  Product.objects.create
#         # productInstance  =  ProductSerializer(data = product_data)
#         productInstance.is_valid(raise_exception=True)
#         product_return = productInstance.save()
#         new_product_inventory = ProductInventory.objects.create(product_id  = product_return, **validated_data)
#         for uploaded_item in uploaded_images:
#             new_product_image = Images.objects.create(product_inventory_id = new_product_inventory, file_name = uploaded_item)
        
#         for attr_value in attributes_value:
#             dict_attribute = json.loads(attr_value)
#             dict_attribute.update({"product_inv_id": new_product_inventory.id})
#             serializer = ProductAttributeValueSerializer(data = dict_attribute)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#         return new_product_inventory

       