# Generated by Django 5.1.3 on 2024-12-27 01:58

import logistics.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0007_course_alter_event_cropping'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, help_text='Tamaño recomendado: 800x400 píxeles. Máximo 2MB.', null=True, upload_to='course_images/', validators=[logistics.validators.validate_image_size], verbose_name='Imagen del Curso'),
        ),
    ]
