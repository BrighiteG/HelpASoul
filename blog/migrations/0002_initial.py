# Generated by Django 4.0 on 2022-01-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
    ]
