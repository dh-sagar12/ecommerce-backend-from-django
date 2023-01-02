from django.db import models
 

class CountryModel(models.Model):

    id  =  models.BigAutoField(primary_key=True, db_column='id')
    iso = models.CharField(max_length=12, db_column='iso')
    country_name = models.CharField(max_length=80, db_column='country_name')
    nice_name  = models.CharField(max_length= 80, db_column='nice_name')
    iso_3 = models.CharField(max_length=13, db_column='iso_3')
    num_code   = models.SmallIntegerField(null=True, db_column='num_code')
    phone_code  = models.IntegerField(null=False, db_column='phone_code')


    def __str__(self):
        return str(self.country_name)



    class Meta: 
        db_table ='core"."country_details'