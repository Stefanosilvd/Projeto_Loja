# Generated by Django 5.2.4 on 2025-07-09 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pagamento",
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
                (
                    "forma",
                    models.CharField(
                        choices=[
                            ("cartao", "Cartão de Crédito"),
                            ("pix", "Pix"),
                            ("boleto", "Boleto"),
                        ],
                        max_length=10,
                    ),
                ),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
