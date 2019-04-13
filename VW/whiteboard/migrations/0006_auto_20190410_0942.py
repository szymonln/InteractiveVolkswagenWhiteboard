# Generated by Django 2.2 on 2019-04-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0005_area_whiteboards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='whiteboards',
        ),
        migrations.AddField(
            model_name='area',
            name='whiteboards',
            field=models.ManyToManyField(blank=True, default=None, to='whiteboard.Whiteboard'),
        ),
    ]
