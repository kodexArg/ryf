# Generated by Django 4.2.6 on 2023-11-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_character_portrait_filename_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='portrait_url',
        ),
        migrations.AddField(
            model_name='character',
            name='portrait_filename',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]