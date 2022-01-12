# Generated by Django 4.0 on 2022-01-12 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social_cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcase',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AddField(
            model_name='donation',
            name='social_case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations_so_far', to='social_cases.socialcase'),
        ),
        migrations.AddField(
            model_name='donation',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
