from django.db import models
from account.models.user import User

from product.models.product import Product
from product.models.productInventory import ProductInventory
from stocks.models.CartModels import CartModel


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
    delivered_date  = models.DateField( null=True,  db_column  = 'delivered_date')
    cart_id   = models.ForeignKey(CartModel, on_delete=models.DO_NOTHING, db_column='cart_id', null=True, to_field='id')


    class Meta:
        db_table ='inventory"."orders'


class DeliveryAdressModel(models.Model):
    id  =  models.BigAutoField(primary_key=True, db_column='id')
    order_id  =  models.ForeignKey(OrdersModel, on_delete=models.DO_NOTHING, db_column='order_id')
    full_name  = models.CharField(max_length=200, db_column='full_name', null=False, blank=False)
    address =  models.CharField(max_length=500, db_column='address', null=False, blank=False)
    landmark =  models.CharField(max_length=400, db_column='landmark')
    postal_code =  models.IntegerField(db_column='postal_code')
    city =  models.CharField(max_length=100, db_column='city')
    contact_number   =  models.CharField(max_length=15, db_column='contact_number', null=False)


    class Meta:
        db_table  =  'inventory"."delivery_addresses'


    

class OrdersStatusModel(models.Model):
    id =  models.BigAutoField(primary_key= True, db_column='id')
    order_id = models.ForeignKey(OrdersModel, on_delete=models.DO_NOTHING, db_column='order_id')
    order_status = models.CharField(max_length=20, blank=False, null=False)
    order_remarks = models.CharField(max_length=200, blank=False, null=False, db_column='order_remarks')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='created_by')
    created_on = models.DateTimeField(auto_now=True, db_column='created_on')
    

    class Meta:
        db_table =  'inventory"."orders_status'
