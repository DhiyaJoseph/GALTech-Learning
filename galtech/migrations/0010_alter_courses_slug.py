# Generated by Django 4.2.7 on 2023-12-13 05:38

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galtech', '0009_courses_slug_alter_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='course_name', unique=True),
        ),
    ]
