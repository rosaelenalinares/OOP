# Generated by Django 2.2.13 on 2021-08-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webshop', '0007_auto_20210827_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('OW', 'Outer wear'), ('AW', 'Active wear'), ('SW', 'Swimwear'), ('CW', 'Casual Wear'), ('B', 'Bottoms'), ('SB', 'Shirt and blouses'), ('SW', 'Sport Wear'), ('SL', 'Sleep wear'), ('S', 'Shoes')], max_length=100, null=True),
        ),
    ]
