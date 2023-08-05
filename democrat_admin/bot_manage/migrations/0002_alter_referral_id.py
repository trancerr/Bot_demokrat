# Generated by Django 4.2.3 on 2023-07-30 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("bot_manage", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referral",
            name="id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="bot_manage.user",
            ),
        ),
    ]