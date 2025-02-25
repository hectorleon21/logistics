# Generated by Django 5.1.3 on 2024-12-27 02:14

import image_cropping.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0008_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '400x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
