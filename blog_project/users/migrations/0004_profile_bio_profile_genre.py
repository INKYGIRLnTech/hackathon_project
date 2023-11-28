# Generated by Django 4.2.7 on 2023-11-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_users_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='genre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]