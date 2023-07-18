# Generated by Django 4.2.3 on 2023-07-07 07:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_query_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=datetime.datetime(2023, 7, 7, 7, 24, 27, 724266)),
        ),
        migrations.AlterField(
            model_name='query',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name=datetime.datetime(2023, 7, 7, 7, 24, 27, 724125)),
        ),
    ]