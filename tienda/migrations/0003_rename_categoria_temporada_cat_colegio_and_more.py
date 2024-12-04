# Generated by Django 5.1.3 on 2024-12-03 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria_Temporada',
            new_name='Cat_Colegio',
        ),
        migrations.RenameModel(
            old_name='Categoria_Tipo',
            new_name='Cat_Sexo',
        ),
        migrations.RenameModel(
            old_name='Categoria_Material',
            new_name='Cat_Tipo',
        ),
        migrations.AlterModelOptions(
            name='cat_colegio',
            options={'verbose_name': 'cat_colegio', 'verbose_name_plural': 'cats_colegios'},
        ),
        migrations.AlterModelOptions(
            name='cat_sexo',
            options={'verbose_name': 'cat_sexo', 'verbose_name_plural': 'cat_sexos'},
        ),
        migrations.AlterModelOptions(
            name='cat_tipo',
            options={'verbose_name': 'cat_tipo', 'verbose_name_plural': 'cat_tipos'},
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categorias_temporada',
            new_name='cat_colegio',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categorias_tipo',
            new_name='cat_sexo',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='categorias_material',
            new_name='cat_tipo',
        ),
    ]
