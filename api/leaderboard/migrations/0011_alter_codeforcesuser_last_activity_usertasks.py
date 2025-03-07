# Generated by Django 5.1.5 on 2025-02-22 12:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("leaderboard", "0010_leetcodeuser_total_solved_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="codeforcesuser",
            name="last_activity",
            field=models.BigIntegerField(default=1740228042.626266),
        ),
        migrations.CreateModel(
            name="UserTasks",
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
                ("problem", models.PositiveIntegerField(default=0)),
                ("dueDate", models.DateTimeField()),
                ("title", models.CharField(max_length=64)),
                ("discription", models.CharField(max_length=256)),
                ("completed", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
