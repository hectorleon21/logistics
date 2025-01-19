# Generated by Django 5.1.3 on 2025-01-04 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0010_newslettersubscription_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersubscription',
            name='region',
            field=models.CharField(blank=True, choices=[('Amazonas', 'Amazonas'), ('Áncash', 'Áncash'), ('Apurímac', 'Apurímac'), ('Arequipa', 'Arequipa'), ('Ayacucho', 'Ayacucho'), ('Cajamarca', 'Cajamarca'), ('Callao', 'Callao'), ('Cusco', 'Cusco'), ('Huancavelica', 'Huancavelica'), ('Huánuco', 'Huánuco'), ('Ica', 'Ica'), ('Junín', 'Junín'), ('La Libertad', 'La Libertad'), ('Lambayeque', 'Lambayeque'), ('Lima', 'Lima'), ('Loreto', 'Loreto'), ('Madre de Dios', 'Madre de Dios'), ('Moquegua', 'Moquegua'), ('Pasco', 'Pasco'), ('Piura', 'Piura'), ('Puno', 'Puno'), ('San Martín', 'San Martín'), ('Tacna', 'Tacna'), ('Tumbes', 'Tumbes'), ('Ucayali', 'Ucayali')], default='Lima', max_length=100, null=True, verbose_name='Región'),
        ),
    ]
