from django.db import models



def upload_to(instance, filename):
    return 'Banners/{filename}'.format(filename=filename)


class BannerPicture(models.Model):
    id  =  models.BigAutoField(primary_key=True, db_column='id') 
    alt_text = models.CharField(db_column ='alt_text', max_length = 100)
    file_name = models.ImageField(upload_to = upload_to)
    redirect_url =  models.CharField(db_column= 'redirect_url', max_length=500)
    is_active =  models.BooleanField(default=True, db_column='is_active')
    created_on = models.DateTimeField(auto_now_add= True, db_column='created_on')

    def __str__(self):
        return str(self.file_name)


    class Meta: 
        db_table ='core"."banner_images'