# Generated by Django 2.2 on 2019-05-10 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0035_auto_20190428_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='path',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 5, 10, 15, 53, 21, 723975, tzinfo=utc)),
        ),
    ]
