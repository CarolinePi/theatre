# Generated by Django 3.1 on 2020-11-30 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_performance_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('editable', 'Can be edited'),)},
        ),
        migrations.AlterModelOptions(
            name='performance',
            options={'permissions': (('editable', 'Can be edited'),)},
        ),
        migrations.AlterModelOptions(
            name='play',
            options={'permissions': (('editable', 'Can be edited'),)},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'permissions': (('editable', 'Can be edited'),)},
        ),
    ]
