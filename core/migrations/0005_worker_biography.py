# Generated by Django 3.1 on 2020-11-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201130_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='biography',
            field=models.TextField(null=True),
        ),
    ]
