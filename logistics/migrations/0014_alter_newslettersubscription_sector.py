# Generated by Django 5.1.3 on 2025-01-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0013_remove_newslettersubscription_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersubscription',
            name='sector',
            field=models.CharField(blank=True, choices=[('Aficiones y casinos', 'Aficiones y casinos'), ('Agricultura y ganadería', 'Agricultura y ganadería'), ('Agua y aguas residuales', 'Agua y aguas residuales'), ('Alimentos', 'Alimentos'), ('Arquitectura', 'Arquitectura'), ('Arte y cultura', 'Arte y cultura'), ('Asistencia y cuidados', 'Asistencia y cuidados'), ('Banca y AFP', 'Banca y AFP'), ('Bebidas alcohólicas', 'Bebidas alcohólicas'), ('Bebidas sin alcohol', 'Bebidas sin alcohol'), ('Centros comerciales y outlets', 'Centros comerciales y outlets'), ('Combustibles fósiles', 'Combustibles fósiles'), ('Comercio al por mayor', 'Comercio al por mayor'), ('Comercio electrónico', 'Comercio electrónico'), ('Comercio internacional', 'Comercio internacional'), ('Construcción naval', 'Construcción naval'), ('Cosmética y cuidado personal', 'Cosmética y cuidado personal'), ('Deporte, fitness y ocio', 'Deporte, fitness y ocio'), ('Educación y ciencia', 'Educación y ciencia'), ('Electrónica', 'Electrónica'), ('Energía y medio ambiente', 'Energía y medio ambiente'), ('Equipamiento del hogar', 'Equipamiento del hogar'), ('Estado de salud', 'Estado de salud'), ('Ferreterías y Bricolage', 'Ferreterías y Bricolage'), ('Finanzas, seguros y bienes inmuebles', 'Finanzas, seguros y bienes inmuebles'), ('Gestión de residuos', 'Gestión de residuos'), ('Hospitales, farmacias y médicos', 'Hospitales, farmacias y médicos'), ('Industria aeroespacial', 'Industria aeroespacial'), ('Industria de defensa', 'Industria de defensa'), ('Industria de software', 'Industria de software'), ('Industria farmacéutica', 'Industria farmacéutica'), ('Ingeniería', 'Ingeniería'), ('Ingeniería civil', 'Ingeniería civil'), ('Juegos de azar', 'Juegos de azar'), ('Juguetes', 'Juguetes'), ('Mascotas', 'Mascotas'), ('Material de oficina', 'Material de oficina'), ('Metalurgia y electrónica', 'Metalurgia y electrónica'), ('Minería, metales y minerales', 'Minería, metales y minerales'), ('Ministerios y Gobierno', 'Ministerios y Gobierno'), ('Mobiliario', 'Mobiliario'), ('Operador Logístico', 'Operador Logístico'), ('Papel y pasta de papel', 'Papel y pasta de papel'), ('Parques y actividades al aire libre', 'Parques y actividades al aire libre'), ('Pesca y acuicultura', 'Pesca y acuicultura'), ('Plástico y caucho', 'Plástico y caucho'), ('Producción de vehículos', 'Producción de vehículos'), ('Productos de limpieza', 'Productos de limpieza'), ('Productos minerales no metálicos', 'Productos minerales no metálicos'), ('Productos químicos y materias primas', 'Productos químicos y materias primas'), ('Publicidad y marketing', 'Publicidad y marketing'), ('Refinerías de petróleo', 'Refinerías de petróleo'), ('Ropa y complementos', 'Ropa y complementos'), ('Salud e higiene', 'Salud e higiene'), ('Sector inmobiliario', 'Sector inmobiliario'), ('Tecnología médica', 'Tecnología médica'), ('Tecnología medioambiental', 'Tecnología medioambiental'), ('Tecnología y telecomunicaciones', 'Tecnología y telecomunicaciones'), ('Turismo y hostelería', 'Turismo y hostelería'), ('Otro', 'Otro')], max_length=100, null=True, verbose_name='Sector'),
        ),
    ]
