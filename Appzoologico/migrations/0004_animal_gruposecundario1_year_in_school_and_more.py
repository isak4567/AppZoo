# Generated by Django 4.1.2 on 2022-11-12 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appzoologico', '0003_remove_animal_gruposecundario1_mandibula_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal_gruposecundario1',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
        migrations.AddField(
            model_name='animal_gruposecundario2',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
    ]
