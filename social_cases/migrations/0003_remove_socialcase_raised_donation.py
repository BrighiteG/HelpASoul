# Generated by Django 4.0 on 2022-01-12 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social_cases', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialcase',
            name='raised',
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raised', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('social_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_cases.socialcase')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
