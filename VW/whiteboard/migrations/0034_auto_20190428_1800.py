# Generated by Django 2.2 on 2019-04-28 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0033_auto_20190428_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 28, 18, 0, 43, 785420, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
