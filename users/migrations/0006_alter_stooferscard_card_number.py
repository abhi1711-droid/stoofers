# Generated by Django 4.0.5 on 2022-09-19 16:36

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_stooferscard_card_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stooferscard",
            name="card_number",
            field=models.CharField(
                default=users.models.generate_card, max_length=10, unique=True
            ),
        ),
    ]
