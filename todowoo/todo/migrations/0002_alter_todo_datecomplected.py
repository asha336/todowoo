# Generated by Django 4.0.2 on 2022-10-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='datecomplected',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
