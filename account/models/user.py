
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from home.models.CountryModel import CountryModel


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name,  last_name, password=None, password2 = None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name= first_name,
            last_name = last_name
        )


        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, first_name,  last_name,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email= email,
            first_name= first_name,
            last_name= last_name,
            password= password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user







class GenderModel(models.Model):
    id  =  models.BigAutoField(primary_key=True, db_column='id')
    gender_name  =  models.CharField(max_length=50, db_column='gender_name', null=False, blank=False)

    class Meta:
        db_table =   'core"."genders'
    

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True, db_column='id')
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        db_column= 'email'
    )
    password =  models.TextField(null=False, db_column='password')
    first_name = models.CharField(max_length=20, db_column='first_name')
    middle_name = models.CharField(max_length=20, null=True, db_column='middle_name', blank=True)
    last_name =models.CharField(max_length=20, db_column='last_name')
    gender_id  = models.ForeignKey(GenderModel, on_delete=models.DO_NOTHING, null=False, db_column= 'gender_id', to_field='id')
    country_id  =  models.ForeignKey(CountryModel, on_delete=models.DO_NOTHING, null=False, db_column='country_id', to_field='id')
    contact = models.CharField(max_length=20,  db_column='contact')
    dob = models.DateField(db_column='dob')
    is_active = models.BooleanField(default=True, db_column='is_active', null= False)
    is_admin = models.BooleanField(default=False, db_column = 'is_admin', null=False)
    is_customer = models.BooleanField(db_column='is_customer', default=True, null=False)
    is_vendor = models.BooleanField(db_column='is_vendor', default=False, null=False)
    is_verified =  models.BooleanField(default=False, db_column='is_verified',  null=False)
    created_on = models.DateTimeField(auto_now_add= True, db_column='created_on')
    updated_on  =  models.DateTimeField(auto_now=True, db_column='updated_on')
    last_login = models.DateTimeField(db_column='last_login')
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table ='auth"."users'




class ShippingDetailMOdel(models.Model):
    id  =  models.BigAutoField(primary_key=True, db_column='id')
    user_id  =  models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='user_id')
    full_name  = models.CharField(max_length=200, db_column='full_name', null=False, blank=False)
    address =  models.CharField(max_length=500, db_column='address', null=False, blank=False)
    landmark =  models.CharField(max_length=400, db_column='landmark')
    postal_code =  models.IntegerField(db_column='postal_code')
    city =  models.CharField(max_length=100, db_column='city')
    contact_number   =  models.CharField(max_length=15, db_column='contact_number', null=False)


    class Meta:
        db_table  =  'auth"."shipping_details'