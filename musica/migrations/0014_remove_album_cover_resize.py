# Generated by Django 3.2.9 on 2021-12-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0013_auto_20211208_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='cover_resize',
        ),
    ]