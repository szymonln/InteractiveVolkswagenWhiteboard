# Generated by Django 2.2 on 2019-04-13 14:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0016_auto_20190413_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='date_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 4, 13, 14, 40, 40, 279801, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(upload_to='2019-04-13/None'),
        ),
    ]