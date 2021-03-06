# Generated by Django 4.0.4 on 2022-05-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('email', models.EmailField(db_column='email', max_length=255, unique=True, verbose_name='Email')),
                ('password', models.TextField(db_column='password')),
                ('contact', models.PositiveIntegerField(db_column='contact')),
                ('dob', models.DateField(db_column='dob')),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
                ('is_admin', models.BooleanField(db_column='is_admin', default=False)),
                ('is_customer', models.BooleanField(db_column='is_customer')),
                ('is_vendor', models.BooleanField(db_column='is_vendor')),
                ('is_verified', models.BooleanField(db_column='is_verified', default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('updated_on', models.DateTimeField(auto_now=True, db_column='updated_on')),
                ('last_login_on', models.DateTimeField(db_column='last_login_on')),
            ],
            options={
                'db_table': 'auth"."users',
            },
        ),
    ]
