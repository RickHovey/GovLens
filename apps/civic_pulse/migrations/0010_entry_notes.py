# Generated by Django 2.1.11 on 2020-01-22 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("civic_pulse", "0009_auto_20200115_0210"),
    ]

    operations = [
        migrations.AddField(
            model_name="entry", name="notes", field=models.TextField(blank=True),
        ),
    ]
