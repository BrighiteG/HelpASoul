# Generated by Django 4.0 on 2021-12-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_end_date_alter_event_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='profile_image',
            field=models.ImageField(default='static/images/Aesthetic-Desktop-Wallpaper.jpg', upload_to='static/images/dynamic'),
        ),
    ]