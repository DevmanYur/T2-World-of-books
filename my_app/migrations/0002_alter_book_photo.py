# Generated by Django 4.2.13 on 2024-07-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='photo',
            field=models.ImageField(blank=True, help_text='Введите изображение обложки', null=True, upload_to='images', verbose_name='Изображение обложки'),
        ),
    ]