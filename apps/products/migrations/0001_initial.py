# Generated by Django 2.1 on 2018-08-02 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6, verbose_name='Preço')),
                ('amount', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
            ],
            options={
                'verbose_name_plural': 'Produto',
                'ordering': ['-created_at'],
                'get_latest_by': '-created_at',
            },
        ),
    ]