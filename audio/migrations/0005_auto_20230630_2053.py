# Generated by Django 3.2.19 on 2023-06-30 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20230630_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='play_ht',
            name='transcriptionId',
        ),
        migrations.DeleteModel(
            name='Play_ht_webhook',
        ),
    ]
