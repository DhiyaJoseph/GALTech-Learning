# Generated by Django 4.2.7 on 2023-12-13 05:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galtech', '0011_remove_courses_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='course_name', unique=True),
        ),
    ]
