# Generated by Django 4.0 on 2022-01-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_review_social_case'),
        ('social_cases', '0005_remove_socialcase_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcase',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.review'),
        ),
    ]
