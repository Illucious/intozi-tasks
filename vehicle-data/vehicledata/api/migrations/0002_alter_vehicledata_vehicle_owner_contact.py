# Generated by Django 5.0.6 on 2024-05-23 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicledata",
            name="vehicle_owner_contact",
            field=models.BigIntegerField(),
        ),
    ]
