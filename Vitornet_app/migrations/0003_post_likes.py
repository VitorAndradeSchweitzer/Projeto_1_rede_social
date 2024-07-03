# Generated by Django 5.0.6 on 2024-06-24 15:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vitornet_app', '0002_rename_posts2_post'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blog_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
