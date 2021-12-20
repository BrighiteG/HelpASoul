# Generated by Django 4.0 on 2021-12-20 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('social_cases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcase',
            name='profile_image',
            field=models.ImageField(default='static/images/Aesthetic-Desktop-Wallpaper.jpg', upload_to='static/images/dynamic'),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('social_case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_cases.socialcase')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
