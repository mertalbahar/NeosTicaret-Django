# Generated by Django 4.2.1 on 2023-05-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='productImage',
            field=models.FileField(blank=True, null=True, upload_to='products/', verbose_name='Ürün Resmi'),
        ),
    ]
