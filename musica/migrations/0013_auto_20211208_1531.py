# Generated by Django 3.2.9 on 2021-12-08 14:31

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0012_auto_20211208_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='cover_resize',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[240, 240], upload_to='imagenes'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes'),
        ),
    ]
