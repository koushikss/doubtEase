# Generated by Django 4.2.4 on 2023-08-15 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='rooms',
        ),
    ]
