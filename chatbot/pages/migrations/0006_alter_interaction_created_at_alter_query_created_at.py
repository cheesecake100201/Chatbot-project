# Generated by Django 4.2.3 on 2023-07-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_interaction_created_at_alter_query_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='query',
            name='created_at',
            field=models.DateTimeField(null=True),
        ),
    ]