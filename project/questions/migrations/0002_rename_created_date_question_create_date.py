# Generated by Django 5.1.1 on 2024-11-05 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='created_date',
            new_name='create_date',
        ),
    ]
