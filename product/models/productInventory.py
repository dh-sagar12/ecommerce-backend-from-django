from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify
from product.models.brands import Brands

from product.models.product import Product

# Create your models here.

class ProductInventory(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    sku = models.BigIntegerField(max_length=10, db_column='sku')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, to_field='id', db_column= 'product_id')
    brand_id = models.ForeignKey(Brands, on_delete=models.DO_NOTHING, to_field='id', db_column= 'brand_id')
    is_active =  models.BooleanField(default=True, db_column='is_active', null=False)
    
    is_default =  models.BooleanField(default=False, db_column='is_default', null=False)

    store_price =  models.BigIntegerField(null=False, blank=False, db_column='store_price')

    discount =  models.IntegerField(null=True, db_column='discount')    

    retail_price =  models.IntegerField(null=False, db_column='retail_price')

    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on') 
    updated_on = models.DateTimeField(auto_now=True, db_column='updated_on') 

    class Meta:
        db_table ='product"."product_inventory'
