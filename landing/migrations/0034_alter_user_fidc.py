# Generated by Django 5.0.7 on 2024-07-12 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0033_alter_user_fidc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fidc',
            field=models.UUIDField(default=257380405183082061311811615884203446589, unique=True),
        ),
    ]
