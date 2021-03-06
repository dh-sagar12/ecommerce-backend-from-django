from operator import mod
from pyexpat import model
from unicodedata import category
from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    slug = models.SlugField(db_column='slug', unique=True)
    category_name= models.CharField(max_length=150, db_column='category_name', null=False)
    is_active = models.BooleanField(default=True, db_column='is_active')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on') 

    
    def __str__(self):
        return str(self.category_name)
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)


    
    class Meta:
        db_table ='product"."category'

    

class SubCategory(models.Model):
    id =  models.AutoField(primary_key=True, db_column='id')
    sub_category_name = models.CharField(max_length=50, null=False, blank=False, db_column='sub_category_name')
    slug =  models.SlugField(db_column='slug',  unique=True)
    category_id =  models.ForeignKey(Category, to_field='id',on_delete=models.DO_NOTHING, db_column='category_id')
    is_active = models.BooleanField(default=True, db_column='is_active')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on')

    
    def __str__(self):
        return str(self.sub_category_name)

    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.sub_category_name)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'product"."sub_category'
