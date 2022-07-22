import random
from django.db import models
from django.template.defaultfilters import slugify
from product.models.product import Product

# Create your models here.

class ProductInventory(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    sku = models.CharField(max_length=12, db_column='sku', unique=True)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, to_field='id', db_column= 'product_id')
    is_active =  models.BooleanField(default=True, db_column='is_active', null=False)
    is_default =  models.BooleanField(default=False, db_column='is_default', null=False)
    store_price =  models.BigIntegerField(null=False, blank=False, db_column='store_price')
    discount =  models.IntegerField(null=True, db_column='discount')    
    retail_price =  models.IntegerField(null=False, db_column='retail_price')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on') 
    updated_on = models.DateTimeField(auto_now=True, db_column='updated_on') 

    def save(self, *args, **kwargs):  # new
        if not self.sku:
            self.sku = create_sku()
        return super().save(*args, **kwargs)


    class Meta:
        db_table ='product"."product_inventory'


def create_sku():
    secretstring = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''.join((random.choice(secretstring) for x in range(12)))
    return result