# Generated by Django 4.2.16 on 2024-10-17 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_msg_senton'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='senton',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 5, 57, 21, 638742)),
        ),
    ]
