# Generated by Django 4.0.4 on 2022-06-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0007_merge_20220623_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupoinvestigacion',
            name='integrantes',
            field=models.ManyToManyField(
                related_name='%(class)s_integrantes', to='investigadores.investigador'),
        ),
    ]
