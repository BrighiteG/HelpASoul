# Generated by Django 4.0 on 2022-01-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0005_newsletter_newsletter_tag_subscriber_subscriber_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
