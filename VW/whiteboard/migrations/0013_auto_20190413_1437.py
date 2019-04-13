# Generated by Django 2.2 on 2019-04-13 14:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0012_auto_20190413_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 13, 14, 37, 46, 104540, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='owner',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
