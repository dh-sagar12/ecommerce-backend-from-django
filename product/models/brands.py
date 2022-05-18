from django.db import models


class Brands(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name= models.CharField(max_length=150, db_column='name', null=False)
    description =  models.TextField(max_length=1000, db_column='description')
    is_active = models.BooleanField(default=True, db_column='is_active')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on') 

    def __str__(self):
        return str(self.name)
    


    class Meta:
        db_table ='product"."brands'
