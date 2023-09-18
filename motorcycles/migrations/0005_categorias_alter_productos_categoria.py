# Generated by Django 4.2.4 on 2023-08-31 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("motorcycles", "0004_alter_productos_categoria_delete_categorias"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categorias",
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
                ("nombre", models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name="productos",
            name="categoria",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="motorcycles.categorias"
            ),
        ),
    ]
