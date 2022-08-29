
from django.db  import models
from product.models.product import Product

from product.models.productInventory import ProductInventory

def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)

class Images(models.Model):
    id  =  models.BigAutoField(primary_key=True, db_column='id')
    product_inventory_id  =  models.ForeignKey(ProductInventory, on_delete=models.DO_NOTHING, db_column='product_inventory_id', related_name='images')
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING, db_column='product_id', related_name='image', null=True)
    file_name = models.ImageField(upload_to = upload_to)
    created_on = models.DateTimeField(auto_now_add= True, db_column='created_on')

    def __str__(self):
        return str(self.file_name)


    class Meta: 
        db_table ='product"."images'
