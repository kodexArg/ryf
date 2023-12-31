# Generated by Django 4.2.6 on 2023-11-05 19:39

import api.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physique', models.IntegerField()),
                ('intellect', models.IntegerField()),
                ('skill', models.IntegerField()),
                ('perception', models.IntegerField()),
                ('empathy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(default=api.models.generate_slug, editable=False, max_length=4, unique=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('nick_name', models.CharField(max_length=50, null=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('occupation', models.CharField(max_length=20)),
                ('secret_occupation', models.CharField(blank=True, max_length=20, null=True)),
                ('faction', models.CharField(max_length=20, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('background_secret', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=20, null=True)),
                ('portrait_filename', models.CharField(blank=True, max_length=20, null=True)),
                ('stats', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.stat')),
            ],
        ),
    ]
