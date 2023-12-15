# Generated by Django 4.2.7 on 2023-12-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galtech', '0002_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('fee', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.BooleanField(choices=[(True, 'Paid'), (False, 'Unpaid')], default=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
    ]
