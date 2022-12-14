# Generated by Django 4.1.2 on 2022-11-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appzoologico', '0004_animal_gruposecundario1_year_in_school_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal_gruposecundario1',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='animal_gruposecundario1',
            name='year_in_school',
        ),
        migrations.RemoveField(
            model_name='animal_gruposecundario2',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='animal_gruposecundario2',
            name='year_in_school',
        ),
        migrations.AddField(
            model_name='animal_gruposecundario1',
            name='Especie',
            field=models.CharField(choices=[('Mamifero', 'Mamifero'), ('Aves', 'Aves'), ('Reptil', 'Reptil'), ('Anfibio', 'Anfibio'), ('Pez', 'Pez')], default='Mamifero', max_length=8),
        ),
        migrations.AddField(
            model_name='animal_gruposecundario2',
            name='Especie',
            field=models.CharField(choices=[('Insecto', 'Insecto'), ('Araña', 'Araña'), ('Molusco', 'Molusco'), ('Crustaceo', 'Crustaceo'), ('Myriapoda', 'Myriapoda')], default='Insectos', max_length=9),
        ),
        migrations.AlterField(
            model_name='animal_gruposecundario1',
            name='alimentacion',
            field=models.CharField(choices=[('Omnívoro', 'Omnívoro'), ('Carnívoro', 'Carnívoro'), ('Herbívoro', 'Herbívoro'), ('Insectivoros', 'Insectivoros')], default='Omnívoro', max_length=12),
        ),
        migrations.AlterField(
            model_name='animal_gruposecundario1',
            name='conducta',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='animal_gruposecundario2',
            name='alimentacion',
            field=models.CharField(choices=[('Omnívoro', 'Omnívoro'), ('Carnívoro', 'Carnívoro'), ('Herbívoro', 'Herbívoro'), ('Insectivoros', 'Insectivoros')], default='Omnívoro', max_length=12),
        ),
        migrations.AlterField(
            model_name='animal_gruposecundario2',
            name='conducta',
            field=models.CharField(max_length=45),
        ),
    ]
