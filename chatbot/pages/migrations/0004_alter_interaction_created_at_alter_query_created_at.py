# Generated by Django 4.2.3 on 2023-07-06 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_interaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 10, 45, 3, 356065)),
        ),
        migrations.AlterField(
            model_name='query',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 6, 10, 45, 3, 355954)),
        ),
    ]