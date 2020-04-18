# Generated by Django 3.0.5 on 2020-04-18 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_album_band_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='album',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='musics', to='myapp.Album'),
        ),
    ]
