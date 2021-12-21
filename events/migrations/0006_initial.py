# Generated by Django 4.0 on 2021-12-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0005_remove_tag_social_case_organizer_delete_event_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('organizer', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('profile_image', models.ImageField(default='static/images/Aesthetic-Desktop-Wallpaper.jpg', upload_to='static/images/dynamic')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('event_tags', models.ManyToManyField(to='events.Tag')),
            ],
        ),
    ]