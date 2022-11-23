# Generated by Django 4.1.3 on 2022-11-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(default='Others', max_length=16, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(unique=True, verbose_name='Содержание'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=256, unique=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='author',
            name='alias',
            field=models.CharField(max_length=16, unique=True, verbose_name='Ваш псевдоним'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Ваш адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=16, verbose_name='Ваше имя'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=16, verbose_name='Ваша фамилия'),
        ),
    ]
