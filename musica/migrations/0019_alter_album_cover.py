# Generated by Django 3.2.9 on 2021-12-08 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0018_alter_album_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, default='imagenes/not-found.png', upload_to='imagenes/'),
        ),
    ]
