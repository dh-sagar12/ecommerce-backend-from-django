# Generated by Django 4.0.4 on 2023-01-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_category_thumbnail_img_product_price_option_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.CharField(db_column='description', max_length=200, null=True),
        ),
    ]
