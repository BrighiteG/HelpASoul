# Generated by Django 4.0 on 2022-01-26 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('organisation', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('profile_image', models.ImageField(default='static/images/Aesthetic-Desktop-Wallpaper.jpg', upload_to='static/images/dynamic')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('location', models.CharField(max_length=200, null=True)),
                ('gps_coordinates_long', models.DecimalField(decimal_places=8, default=10.0, max_digits=20)),
                ('gps_coordinates_lat', models.DecimalField(decimal_places=8, default=10.0, max_digits=20)),
                ('event_tags', models.ManyToManyField(to='events.Tag')),
            ],
        ),
    ]
