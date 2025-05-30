# Generated by Django 5.2 on 2025-05-12 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institucion', '0001_initial'),
        ('usuarios', '0003_alter_bitacora_options_alter_superadmin_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='colegio',
            name='super_admin_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='colegios', to='usuarios.superadmin'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='colegio_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modulos', to='institucion.colegio'),
        ),
        migrations.AddField(
            model_name='unidadeducativa',
            name='admin_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unidades_educativas', to='usuarios.admin'),
        ),
        migrations.AddField(
            model_name='unidadeducativa',
            name='nivel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unidadeducativa',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='aula',
            name='modulo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aulas', to='institucion.modulo'),
        ),
        migrations.AlterField(
            model_name='unidadeducativa',
            name='colegio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unidades_educativas', to='institucion.colegio'),
        ),
    ]
