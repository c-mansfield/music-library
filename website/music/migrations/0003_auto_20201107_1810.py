# Generated by Django 2.2.5 on 2020-11-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_art',
            field=models.FileField(upload_to=''),
        ),
    ]
