# Generated by Django 2.2.13 on 2021-08-27 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webshop', '0008_auto_20210827_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Outer wear', 'Outer wear'), ('Active wear', 'Active wear'), ('Swimwear', 'Swimwear'), ('Casual Wear', 'Casual Wear'), ('Bottoms', 'Bottoms'), ('Shirt and blouses', 'Shirt and blouses'), ('Sport Wear', 'Sport Wear'), ('Sleep wear', 'Sleep wear'), ('Shoes', 'Shoes')], max_length=100, null=True),
        ),
    ]