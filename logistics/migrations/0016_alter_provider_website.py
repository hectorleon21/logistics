# Generated by Django 5.1.3 on 2025-02-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0015_alter_course_modality_alter_provider_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provider',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sitio Web'),
        ),
    ]
