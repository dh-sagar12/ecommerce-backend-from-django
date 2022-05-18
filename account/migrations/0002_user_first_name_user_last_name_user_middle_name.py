# Generated by Django 4.0.4 on 2022-05-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(db_column='first_name', default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(db_column='last_name', default='admin', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(db_column='middle_name', default='asdfj', max_length=20),
            preserve_default=False,
        ),
    ]
