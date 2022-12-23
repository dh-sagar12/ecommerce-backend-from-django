from django.db import models
from account.models.user import User

from product.models.product import Product
from product.models.productInventory import ProductInventory


class OrdersModel(models.Model):

    id  = models.AutoField(primary_key=True, db_column='id')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, to_field='id', db_column='product_id')
    product_inventory_id = models.ForeignKey(ProductInventory, on_delete=models.DO_NOTHING, to_field='id', db_column='product_inventory_id')
    order_qty = models.BigIntegerField(null=False, blank= False,  db_column = 'order_qty')
    ordered_by =  models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='ordered_by', to_field='id')
    ordered_date  = models.DateField(auto_now_add =  True, db_column  = 'ordered_date')
    payment_method   = models.BigIntegerField(null=False, blank=False, db_column = 'payment_method')
    is_payment_completed  =  models.BooleanField(default=False, null=False, db_column="is_payment_completed")
    created_on  = models.DateField(auto_now_add =  True, db_column  = 'created_on')
    updated_on  = models.DateField(auto_now_add =  True, db_column  = 'updated_on')
    delivered_date  = models.DateField(auto_now_add =  True, db_column  = 'delivered_date')



    class Meta:
        db_table ='inventory"."orders'