# Generated by Django 4.1.7 on 2023-03-30 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_delete_userfollowing'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-creation_date',)},
        ),
    ]
