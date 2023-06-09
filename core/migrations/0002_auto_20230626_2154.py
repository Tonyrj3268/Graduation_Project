# Generated by Django 3.2.19 on 2023-06-26 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='userID',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='fileLocation',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('0', '未處理'), ('1', '文字稿生成完成'), ('2', 'Deepl翻譯完成'), ('3', 'Play.ht語音生成完成'), ('4', '任務完成'), ('-1', '任務失敗'), (None, 'N/A')], max_length=50),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
