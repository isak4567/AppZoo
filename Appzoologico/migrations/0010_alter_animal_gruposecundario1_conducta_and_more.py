# Generated by Django 4.1.2 on 2022-11-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appzoologico', '0009_animal_gruposecundario1_imagenanimal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal_gruposecundario1',
            name='conducta',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='animal_gruposecundario2',
            name='conducta',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='descripcion',
            field=models.TextField(default='', max_length=300),
        ),
    ]
