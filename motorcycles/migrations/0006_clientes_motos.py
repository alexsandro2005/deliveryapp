# Generated by Django 4.2.4 on 2023-09-03 23:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("motorcycles", "0005_categorias_alter_productos_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Clientes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("documento", models.CharField(max_length=10, unique=True)),
                ("nombres", models.CharField(max_length=100)),
                ("telefono", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=100)),
                ("genero", models.CharField(max_length=100)),
                (
                    "fecha_registro",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Motos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("placa", models.CharField(max_length=6, unique=True)),
                ("kilometraje", models.IntegerField(max_length=6)),
                ("modelo", models.IntegerField(max_length=4)),
                ("marca", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=50)),
                ("carroceria", models.CharField(max_length=50)),
                ("cilindraje", models.IntegerField(max_length=4)),
                ("combustible", models.CharField(max_length=50)),
                ("uso", models.CharField(max_length=50)),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="motorcycles.clientes",
                    ),
                ),
            ],
        ),
    ]
