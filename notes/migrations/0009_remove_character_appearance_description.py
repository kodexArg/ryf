# Generated by Django 4.2.6 on 2023-11-05 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_character_appearance_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='appearance_description',
        ),
    ]
