# Generated by Django 4.2.3 on 2023-07-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]
