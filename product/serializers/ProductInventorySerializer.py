import json
from rest_framework import serializers
from product.models.Images import Images
from product.models.product import Product
from product.models.productInventory import ProductInventory
from product.serializers.AttributesSerializers import ProductAttributeValueSerializer
from product.serializers.ImageSerializer import ImageSerializer
from django.db import transaction
from PIL import Image

# from .productSerializer import ProductSerializer


# serialzer to used only to add  product items but not attribute and images  
class SingleProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model =  ProductInventory
        fields = ['id', 'sku', 'product_id',  'is_active', 'is_default', 'store_price', 'discount', 'retail_price','created_on', 'updated_on' ]
        read_only_fields = ['id', 'sku', 'created_on',  'updated_on' ]
        





# serializers to be used to create product items including images and attribute but not create product itself. it is basicaly used to add items inside a product 
# for post method only 
class ProductInventorySerializer(serializers.ModelSerializer):
    images  =  ImageSerializer( many=True, read_only=  True)
    attributes =  ProductAttributeValueSerializer(many=  True, read_only =  True)
    
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = True, use_url = True ),
        write_only = True,
        required  =  False
    )

    attributes_value =  serializers.ListField(
        child =  serializers.JSONField(),
        write_only =  True, 
        required =  False
    )
    
    
    class Meta:
        model = ProductInventory
        fields = ['id', 'sku', 'product_id',  'is_active', 'is_default', 'store_price', 'discount', 'retail_price', 'images', 'uploaded_images', 'attributes', 'attributes_value', 'created_on', 'updated_on' ]
        read_only_fields = ['id', 'sku', 'created_on', 'images' , 'updated_on' , 'attributes']

    @transaction.atomic
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images')
        print('uploaded_images', uploaded_images)
        attributes_value =  validated_data.pop('attributes_value')
        new_product_inventory = ProductInventory.objects.create(**validated_data)
        for uploaded_item in uploaded_images:
            new_product_image = Images.objects.create(product_inventory_id = new_product_inventory, file_name = uploaded_item, product_id= new_product_inventory.product_id)
        
        for attr_value in attributes_value:
            dict_attribute = json.loads(attr_value)
            dict_attribute.update({"product_inv_id": new_product_inventory.id})
            serializer = ProductAttributeValueSerializer(data = dict_attribute)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return new_product_inventory


    @transaction.atomic
    def update(self, instance, validated_data):
        uploaded_images   =  validated_data.get('uploaded_images')
        attributes_value =  validated_data.get('attributes_value')
        product_item_instance  =  ProductInventory.objects.get(id= instance.get('id'))
        product_instance  = Product.objects.get(id=instance.get('product_id') )
        serializer =  SingleProductItemSerializer(product_item_instance, data=instance, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if uploaded_images is not None:
            for uploaded_item in uploaded_images:
                Images.objects.create(product_inventory_id = product_item_instance, file_name = uploaded_item, product_id= product_instance)

        if  attributes_value is not None:
            for attr_value in attributes_value:
                dict_attribute = json.loads(attr_value)
                if len(dict_attribute) > 0:
                    dict_attribute.update({"product_inv_id": instance.get('id')})
                    serializer = ProductAttributeValueSerializer(data = dict_attribute)
                    serializer.is_valid(raise_exception=True)
                    serializer.save()
        
        return True


# serialzer to create only product inventory not any other items in it 




class ProductInventorySerializerForGetMethod(ProductInventorySerializer):
    images  =  ImageSerializer(source= 'image_list', many=True, read_only=  True)

    class Meta(ProductInventorySerializer.Meta):
        model =  ProductInventorySerializer.Meta.model
        fields = ProductInventorySerializer.Meta.fields
        read_only_fields =  ProductInventorySerializer.Meta.read_only_fields
        depth = 1