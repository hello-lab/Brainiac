# Generated by Django 5.0.7 on 2024-07-13 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0039_rename_id_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
