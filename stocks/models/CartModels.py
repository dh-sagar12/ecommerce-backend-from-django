from django.db import models
from account.models.user import User

from product.models.product import Product
from product.models.productInventory import ProductInventory
from stocks.models.OrderModels import OrdersModel


class CartModel(models.Model):

    id  = models.AutoField(primary_key=True, db_column='id')
    user_id =  models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id', to_field='id')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, to_field='id', db_column='product_id')
    product_inventory_id = models.ForeignKey(ProductInventory, on_delete=models.DO_NOTHING, to_field='id', db_column='product_inventory_id')
    cart_qty = models.BigIntegerField(null=False, blank= False,  db_column = 'cart_qty')
    status  =  models.BooleanField(default=True, null=False, db_column="status")
    order_id =  models.ForeignKey(OrdersModel, on_delete=models.DO_NOTHING, to_field='id', db_column='order_id', null=True )
    created_on  = models.DateTimeField(auto_now_add =  True, db_column  = 'created_on')

    class Meta:
        db_table ='inventory"."cart'