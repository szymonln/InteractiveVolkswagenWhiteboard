# Generated by Django 2.2 on 2019-04-13 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0020_auto_20190413_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='whiteboard',
            field=models.ForeignKey(default=True, null=True, on_delete=models.SET(None), to='whiteboard.Whiteboard'),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 13, 16, 46, 26, 514978, tzinfo=utc)),
        ),
    ]
