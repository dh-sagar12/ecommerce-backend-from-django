# Generated by Django 4.0.4 on 2022-08-12 13:05

from django.db import migrations, models
import django.db.models.deletion
import product.models.Images


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_productinventory_brand_id_product_brand_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('file_name', models.ImageField(upload_to=product.models.Images.upload_to)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('product_inventory_id', models.ForeignKey(db_column='product_inventory_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='product.productinventory')),
            ],
            options={
                'db_table': 'product"."images',
            },
        ),
    ]
