# Generated by Django 4.0 on 2022-01-10 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_cases', '0016_remove_donation_target_donation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='amount',
            new_name='raised',
        ),
    ]