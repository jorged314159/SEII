# Generated by Django 4.1.3 on 2023-01-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_auto_20230120_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocatoria',
            name='activa',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
