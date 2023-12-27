# Generated by Django 4.1 on 2023-12-20 01:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User_tbl",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=50, primary_key=True, serialize=False),
                ),
                ("user_pwd", models.CharField(max_length=50)),
                ("user_name", models.CharField(max_length=50)),
                ("user_point", models.IntegerField(default=1000)),
                ("user_img", models.CharField(max_length=50)),
            ],
        ),
    ]