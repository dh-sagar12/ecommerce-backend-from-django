from uuid import uuid4
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name= models.CharField(max_length=150, db_column='name', null=False)
    slug = models.SlugField(db_column='slug', unique=True)
    parent =  models.BigIntegerField(db_column='parent')
    is_active = models.BooleanField(default=True, db_column='is_active')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on') 

    
    def __str__(self):
        return str(self.name)
    
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    
    class Meta:
        db_table ='product"."category'
