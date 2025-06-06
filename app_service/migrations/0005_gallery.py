# Generated by Django 5.2 on 2025-05-24 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_service', '0004_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='gallery/', verbose_name='Изображение')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
            options={
                'verbose_name': 'Изображение галереи',
                'verbose_name_plural': 'Галерея изображений',
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
