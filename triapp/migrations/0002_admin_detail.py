# Generated by Django 4.1.5 on 2023-03-12 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("triapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="admin_detail",
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
                ("a_Name", models.CharField(default="", max_length=100)),
                ("a_Email", models.EmailField(default="", max_length=100)),
                (
                    "a_password",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
            ],
        ),
    ]
