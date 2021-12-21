# Generated by Django 4.0 on 2021-12-21 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0006_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_nr', models.IntegerField()),
                ('location', models.CharField(max_length=200)),
                ('is_volunteer', models.BooleanField(default=False)),
                ('profile_tags', models.ManyToManyField(to='events.Tag')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
