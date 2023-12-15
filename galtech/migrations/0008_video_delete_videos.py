# Generated by Django 4.2.7 on 2023-12-11 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galtech', '0007_alter_videos_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('video_title', models.CharField(max_length=50)),
                ('video_upload_url', models.CharField(help_text='Video location name', max_length=250)),
                ('duration', models.CharField(max_length=20)),
                ('thumbnail', models.CharField(help_text='Thumbnail location name', max_length=250)),
                ('note', models.TextField(blank=True, null=True)),
                ('video_file', models.CharField(help_text='Video location name', max_length=250)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='galtech.lessons')),
            ],
        ),
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
