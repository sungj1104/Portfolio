# Generated by Django 5.0.1 on 2024-01-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="thumbnail",
            field=models.ImageField(
                blank=True, upload_to="post", verbose_name="썸네일 이미지"
            ),
        ),
    ]
