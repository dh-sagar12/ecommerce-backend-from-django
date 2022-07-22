from django.db import models

from product.models.category import SubCategory
from product.models.productInventory import ProductInventory




class Attribute(models.Model):
    id  = models.AutoField(primary_key=True, db_column='id')
    attribute_name =  models.CharField(max_length=50, null=False, blank=False, db_column='attribute_name')
    is_active =  models.BooleanField(default=True, null=False, db_column='is_active')

    class Meta:
        db_table ='product"."attributes'

    def __str__(self):
        return self.attribute_name


class CategoryAttribute(models.Model):
    id  = models.AutoField(primary_key=True, db_column='id')
    sub_category_id = models.ForeignKey(SubCategory, on_delete=models.DO_NOTHING, to_field='id', db_column='sub_category_id')
    attribute_id = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING, to_field='id', db_column='attribute_id')

    class Meta:
        db_table ='product"."category_attributes'



class ProductAttributeValues(models.Model):
    id  = models.AutoField(primary_key=True, db_column='id')
    product_inv_id = models.ForeignKey(ProductInventory, on_delete=models.DO_NOTHING, to_field='id', db_column='product_inv_id')

    attribute_id = models.ForeignKey(Attribute, on_delete=models.DO_NOTHING, to_field='id', db_column='attribute_id')

    attribute_value =  models.CharField(max_length=30, null=False, blank=False, db_column='attribute_value')

    class Meta:
        db_table ='product"."product_attribute_values'