# Generated by Django 4.2.6 on 2023-10-31 00:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_imo', '0002_produto_vendas_vendedor_delete_site_vendas_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 30, 21, 46, 16, 604340)),
        ),
    ]