# Generated by Django 4.2.6 on 2023-11-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_character_portrait_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
