# Generated by Django 3.2.9 on 2021-11-17 18:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('pais', models.CharField(blank=True, max_length=50, verbose_name='País')),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('duracion', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Duración')),
            ],
        ),
        migrations.CreateModel(
            name='Discografica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Direccion')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título album')),
                ('fecha_salida', models.DateField(blank=True)),
                ('formato', models.CharField(choices=[('VNL', 'Vinilo'), ('CD', 'Compact Disc'), ('CST', 'Cassette')], max_length=3)),
                ('genero', models.CharField(blank=True, max_length=200)),
                ('duracion', models.DecimalField(blank=True, decimal_places=2, max_digits=6, verbose_name='Duración total')),
                ('artistas', models.ManyToManyField(to='musica.Artista')),
                ('canciones', models.ManyToManyField(to='musica.Cancion')),
                ('discografica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musica.discografica')),
            ],
        ),
    ]
