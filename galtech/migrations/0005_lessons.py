# Generated by Django 4.2.7 on 2023-12-05 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galtech', '0004_courses_delete_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='lessons',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('lesson_title', models.CharField(max_length=50)),
                ('lesson_order', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galtech.courses')),
            ],
        ),
    ]
