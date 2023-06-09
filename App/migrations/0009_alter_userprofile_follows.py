# Generated by Django 4.1.7 on 2023-03-30 14:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App', '0008_alter_userprofile_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='follows',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
