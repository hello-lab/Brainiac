# Generated by Django 5.0.7 on 2024-07-13 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0041_rename_uid_user_id_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subjects',
            field=models.CharField(default='physics,math,chemistry', max_length=300),
        ),
    ]
