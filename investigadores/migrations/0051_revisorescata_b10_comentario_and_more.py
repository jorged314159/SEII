# Generated by Django 4.1.3 on 2024-02-07 21:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0050_categoriaa_b10_categoriaa_b3_categoriaa_b5_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='revisorescata',
            name='b10_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B10.'),
        ),
        migrations.AddField(
            model_name='revisorescata',
            name='b3_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B3.'),
        ),
        migrations.AddField(
            model_name='revisorescata',
            name='b5_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B5.'),
        ),
        migrations.AddField(
            model_name='revisorescata',
            name='b6_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B6.'),
        ),
        migrations.AddField(
            model_name='revisorescata',
            name='b7_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B7.'),
        ),
        migrations.AddField(
            model_name='revisorescata',
            name='b8_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B8.'),
        ),
        migrations.AddField(
            model_name='revisorescata',
            name='b9_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B9.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a1',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A1 - Artículos científicos en revistas indexadas o arbitradas.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a10',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A10 - Pertenencia al Sistema Nacional de Investigadores.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a10_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A10.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a1_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A1.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a2',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A2 - Autoría y coautoría de libros y/o capítulos de libros científicos con arbitraje.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a2_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A2.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a3',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A3 - Trámite de solicitud u obtención de patentes.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a3_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A3.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a4',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A4 - Trámite de solicitud u obtención de derechos de obtentor.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a4_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A4.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a5',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A5 - Desarrollo de software/hardware con Derechos de Autor.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a5_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A5.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a6',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A6 - Implementaciones tecnológicas'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a6_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A6.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a7',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A7 - Artículos o notas científicas publicadas en revistas arbitradas de divulgación científica o tecnológica.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a7_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A7.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a8',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A8 - Participación en proyectos de investigación, desarrollo tecnológico e innovación con financiamiento externo obtenido mediante convocatoria.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a8_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A8.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a9',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='A9 - Editor, compilador o coordinador de libros colectivos.'),
        ),
        migrations.AlterField(
            model_name='revisorescata',
            name='a9_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo A9.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b10',
            field=models.PositiveIntegerField(default=0, verbose_name='B10 - Evaluación de trabajos de investigación o proyectos.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b10_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B10.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b1_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B1.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b2_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B2.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b3',
            field=models.PositiveIntegerField(default=0, verbose_name='B3 - Dirección de Tesis o Artículo de Investigación de alumnos graduados en licenciatura, maestría, doctorado o especialidad médica.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b3_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B3.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b4',
            field=models.PositiveIntegerField(default=0, verbose_name='B4 - Dirección de tesis de licenciatura de alumnos graduados en la modalidad de artículo científico.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b4_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B4.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b5',
            field=models.PositiveIntegerField(default=0, verbose_name='B5 - Presentación de ponencias o carteles en eventos científicos, en México o el extranjero.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b5_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B5.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b6_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B6.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b7',
            field=models.PositiveIntegerField(default=0, verbose_name='B7 - Asignaturas con créditos impartidas en Especialidad, Maestría o Doctorado de programas del SNP.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b7_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B7.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b8',
            field=models.PositiveIntegerField(default=0, verbose_name='B8 - Participación en proyectos de investigación con financiamiento interno o externo.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b8_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B8.'),
        ),
        migrations.AlterField(
            model_name='revisorescatb',
            name='b9_comentario',
            field=models.TextField(default='', max_length=2000, verbose_name='Retroalimentación de la documentación enviada correspondiente al campo B9.'),
        ),
    ]
