# Generated by Django 5.0.6 on 2024-05-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="VehicleData",
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
                ("vehicle_type", models.CharField(max_length=100)),
                ("vehicle_company", models.CharField(max_length=100)),
                ("vehicle_model", models.CharField(max_length=100)),
                ("vehicle_plate_number", models.CharField(max_length=50)),
                ("vehicle_color", models.CharField(max_length=50)),
                ("vehicle_owner", models.CharField(max_length=100)),
                ("vehicle_owner_contact", models.CharField(max_length=50)),
            ],
        ),
    ]
