# Generated by Django 3.2.7 on 2022-01-16 13:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20220116_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name=django.contrib.auth.models.User),
        ),
    ]