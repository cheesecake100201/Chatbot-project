# Generated by Django 4.2.3 on 2023-07-07 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_conversation_delete_interaction_remove_query_chat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='created_at',
            field=models.DateTimeField(null=True, verbose_name=datetime.datetime(2023, 7, 7, 7, 17, 37, 821588)),
        ),
    ]