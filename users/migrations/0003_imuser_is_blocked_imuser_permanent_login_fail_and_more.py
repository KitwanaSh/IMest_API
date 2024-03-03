# Generated by Django 4.2.9 on 2024-03-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_imuser_options_alter_imuser_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="imuser",
            name="is_blocked",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="imuser",
            name="permanent_login_fail",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="imuser",
            name="temporal_login_fail",
            field=models.IntegerField(default=0),
        ),
    ]