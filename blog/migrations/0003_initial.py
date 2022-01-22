# Generated by Django 4.0 on 2022-01-22 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
