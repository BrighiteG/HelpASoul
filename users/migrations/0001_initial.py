# Generated by Django 4.0 on 2022-01-26 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_cases', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('blog', '0002_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('professional_areas', models.CharField(blank=True, max_length=100, null=True)),
                ('is_driver', models.BooleanField(default=False)),
                ('is_available_for_emergengy', models.BooleanField(default=False)),
                ('message', models.TextField(blank=True, max_length=1000, null=True)),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
                ('volunteer_tags', models.ManyToManyField(to='events.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('blog_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
                ('event_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('social_case', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='social_cases.socialcase')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_nr', models.IntegerField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_tags', models.ManyToManyField(to='events.Tag')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_participant', models.BooleanField(default=False)),
                ('event_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
