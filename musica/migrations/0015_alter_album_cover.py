# Generated by Django 3.2.9 on 2021-12-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0014_remove_album_cover_resize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, height_field='alto', null=True, upload_to='imagenes/', verbose_name='cover', width_field='ancho'),
        ),
    ]
