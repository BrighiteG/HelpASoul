# Generated by Django 4.0 on 2022-01-13 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('profile_image', models.ImageField(upload_to='static/images/dynamic')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
