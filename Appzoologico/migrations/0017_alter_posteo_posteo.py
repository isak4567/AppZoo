# Generated by Django 4.1.2 on 2022-11-28 00:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appzoologico', '0016_alter_posteo_avatar_url_alter_posteo_posteo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='posteo',
            field=ckeditor.fields.RichTextField(),
        ),
    ]