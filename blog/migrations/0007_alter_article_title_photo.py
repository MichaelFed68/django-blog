# Generated by Django 4.1.3 on 2023-01-01 20:04

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_title_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title_photo',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.get_user_directory_path, verbose_name='Фото'),
        ),
    ]
