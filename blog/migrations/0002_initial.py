# Generated by Django 4.0 on 2022-01-22 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
    ]
