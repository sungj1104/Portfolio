# Generated by Django 5.0.1 on 2024-02-27 00:42

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("title", models.CharField(max_length=100, verbose_name="Todo의 제목")),
                ("description", models.TextField(verbose_name="Todo에 대한 설명")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Todo 생성일자"),
                ),
            ],
        ),
    ]