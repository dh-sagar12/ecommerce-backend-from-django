from email.policy import default
from django.db import models

from product.models.product import Product
from product.models.productInventory import ProductInventory


class StockModel(models.Model):

    id  = models.AutoField(primary_key=True, db_column='id')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, to_field='id', db_column='product_id')

    product_inventory_id = models.ForeignKey(ProductInventory, on_delete=models.DO_NOTHING, to_field='id', db_column='product_inventory_id')

    stock_qty = models.BigIntegerField(null=False, blank= False,  db_column = 'stock_qty')


    statement_reference =  models.CharField(max_length=100, null=False, blank=False, db_column='statement_reference')
    created_on  = models.DateTimeField(auto_now_add =  True, db_column  = 'created_on')
    updated_on  = models.DateTimeField(auto_now =  True, db_column  = 'updated_on')

    class Meta:
        db_table ='inventory"."stocks'