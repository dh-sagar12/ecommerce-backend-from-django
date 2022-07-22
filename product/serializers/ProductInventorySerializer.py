from rest_framework import serializers
from product.models.productInventory import ProductInventory



class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id', 'sku', 'product_id',  'is_active', 'is_default', 'store_price', 'discount', 'retail_price', 'created_on', 'updated_on' ]
        read_only_fields = ['id', 'sku', 'created_on', 'updated_on']

    