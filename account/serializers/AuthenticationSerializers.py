from rest_framework.validators import ValidationError
from rest_framework import serializers
from account.models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

from account.models.user import GenderModel

class UserLoginSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
    model = User
    fields = ['email', 'password']
  

class UserSerializer(serializers.ModelSerializer):
  password  =  serializers.CharField(max_length = 100, write_only = True)
  confirm   = serializers.CharField(max_length = 100, write_only = True)
  class Meta:
    model =  User
    fields =  ['id', 'email',  'first_name', 'confirm', 'middle_name', 'last_name','password', 'gender_id',  'contact', 'dob', 'is_active', 'is_admin', 'is_customer', 'is_vendor', 'is_verified', 'country_id' ]
    read_only_fields = ['id', 'is_active', 'is_customer', 'is_vendor', 'is_verified']



  def validate(self, attrs):
    email_exists = User.objects.filter(email=attrs["email"]).exists()

    if email_exists:
      raise ValidationError('User with this email already exists..')

    elif attrs["password"] != attrs['confirm'] :
      raise ValidationError("Password doesn't Matches")

    return super().validate(attrs)

  
  def create(self, validated_data):
      password = validated_data.pop("password")
      confirm  =  validated_data.pop("confirm")
      user = super().create(validated_data)

      user.set_password(password)

      user.save()

      return user



class GetGenderSerializer (serializers.ModelSerializer):
  class Meta:
    model  =  GenderModel
    fields  =  ["id", "gender_name"]