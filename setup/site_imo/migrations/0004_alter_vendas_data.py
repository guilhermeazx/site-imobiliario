# Generated by Django 4.2.6 on 2023-10-31 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_imo', '0003_alter_vendas_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendas',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 30, 21, 47, 42, 505541)),
        ),
    ]
