# Generated by Django 2.2.13 on 2021-08-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webshop', '0002_auto_20210813_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imageurl',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
