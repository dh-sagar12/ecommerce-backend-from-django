from pyexpat import model
from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify

from product.models.category import Category

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    web_id = models.UUIDField(default=uuid4, editable=True, db_column='web_id')
    slug = models.SlugField(db_column='slug')
    name= models.CharField(max_length=150, db_column='name', null=False)
    description =  models.TextField(max_length=1000, db_column='description')
    category_id = models.ForeignKey(Category, db_column='category_id', to_field='id', on_delete=models.DO_NOTHING)
    is_active = models.BooleanField(default=True, db_column='is_active')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on') 
    updated_on = models.DateTimeField(auto_now=True, db_column='updated_on') 

    
    def __str__(self):
        return (self.name)
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(f'{self.name}{self.web_id}')
        return super().save(*args, **kwargs)


    
    class Meta:
        db_table ='product"."products'