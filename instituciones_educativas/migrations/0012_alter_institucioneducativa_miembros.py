# Generated by Django 4.1.3 on 2022-12-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0024_alter_investigador_imagen'),
        ('instituciones_educativas', '0011_alter_institucioneducativa_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institucioneducativa',
            name='miembros',
            field=models.ManyToManyField(blank=True, to='investigadores.investigador'),
        ),
    ]