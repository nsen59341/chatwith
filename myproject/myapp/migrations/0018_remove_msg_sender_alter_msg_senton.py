# Generated by Django 4.2.16 on 2024-10-17 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_msg_user_alter_msg_senton_alter_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='sender',
        ),
        migrations.AlterField(
            model_name='msg',
            name='senton',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 10, 16, 48, 95755)),
        ),
    ]
