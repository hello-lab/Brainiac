# Generated by Django 5.0.7 on 2024-07-13 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0038_remove_user_address_remove_user_bio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='uid',
        ),
    ]
