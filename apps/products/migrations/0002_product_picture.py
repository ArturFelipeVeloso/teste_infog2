# Generated by Django 2.1 on 2018-08-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product/%Y/%m/', verbose_name='Foto'),
        ),
    ]
