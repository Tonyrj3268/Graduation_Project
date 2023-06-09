# Generated by Django 3.2.19 on 2023-07-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransformedText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.TextField()),
                ('transformed_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
