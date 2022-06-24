# Generated by Django 4.0.4 on 2022-06-23 17:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('slug', models.SlugField(db_column='slug', unique=True)),
                ('category_name', models.CharField(db_column='category_name', max_length=150)),
                ('is_active', models.BooleanField(db_column='is_active', default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
            ],
            options={
                'db_table': 'product"."category',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(db_column='sub_category_name', max_length=50)),
                ('slug', models.SlugField(db_column='slug', unique=True)),
                ('is_active', models.BooleanField(db_column='is_active', default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.DO_NOTHING, to='product.category')),
            ],
            options={
                'db_table': 'product"."sub_category',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('web_id', models.UUIDField(db_column='web_id', default=uuid.uuid4)),
                ('slug', models.SlugField(db_column='slug')),
                ('product_name', models.CharField(db_column='product_name', max_length=150)),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('is_active', models.BooleanField(db_column='is_active', default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('updated_on', models.DateTimeField(auto_now=True, db_column='updated_on')),
                ('category_id', models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.DO_NOTHING, to='product.category')),
                ('sub_category_id', models.ForeignKey(db_column='sub_category_id', on_delete=django.db.models.deletion.DO_NOTHING, to='product.subcategory')),
            ],
            options={
                'db_table': 'product"."products',
            },
        ),
    ]
