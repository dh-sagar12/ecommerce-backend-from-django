# Generated by Django 4.0.4 on 2022-08-19 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='product_id',
            field=models.ForeignKey(db_column='product_id',  on_delete=django.db.models.deletion.DO_NOTHING, related_name='image', to='product.product'),
        ),
        migrations.AlterField(
            model_name='productattributevalues',
            name='product_inv_id',
            field=models.ForeignKey(db_column='product_inv_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='attributes', to='product.productinventory'),
        ),
        migrations.AlterField(
            model_name='productinventory',
            name='product_id',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_items', to='product.product'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category_id',
            field=models.ForeignKey(db_column='category_id', on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub_categories', to='product.category'),
        ),
    ]