# Generated by Django 4.0 on 2022-01-26 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
