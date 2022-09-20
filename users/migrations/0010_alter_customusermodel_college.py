# Generated by Django 4.0.5 on 2022-09-20 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("static_data", "0001_initial"),
        ("users", "0009_alter_customusermodel_college"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customusermodel",
            name="college",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="static_data.college"
            ),
        ),
    ]
