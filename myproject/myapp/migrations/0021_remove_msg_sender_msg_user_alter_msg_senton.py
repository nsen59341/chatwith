# Generated by Django 4.2.16 on 2024-10-17 10:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0020_remove_msg_user_alter_msg_senton'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='sender',
        ),
        migrations.AddField(
            model_name='msg',
            name='user',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='msg',
            name='senton',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 17, 10, 46, 42, 317686)),
        ),
    ]
