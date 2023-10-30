# Generated by Django 4.1.12 on 2023-10-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="STI",
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
                ("input", models.TextField()),
                ("_output", models.TextField()),
            ],
            options={"db_table": "t_STI",},
        ),
    ]
