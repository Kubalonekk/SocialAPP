# Generated by Django 4.1.7 on 2023-03-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(blank=True, to='App.userprofile'),
        ),
    ]
