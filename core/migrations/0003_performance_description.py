# Generated by Django 3.1 on 2020-11-28 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_author_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
