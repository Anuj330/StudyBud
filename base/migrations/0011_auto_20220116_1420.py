# Generated by Django 3.2.7 on 2022-01-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_room_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='message',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
