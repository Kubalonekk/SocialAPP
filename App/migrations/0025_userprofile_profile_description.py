# Generated by Django 4.1.7 on 2023-04-04 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
