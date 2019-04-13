# Generated by Django 2.2 on 2019-04-10 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whiteboard', '0006_auto_20190410_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='area',
            name='user',
        ),
        migrations.RemoveField(
            model_name='whiteboard',
            name='file',
        ),
        migrations.AddField(
            model_name='area',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='area',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='whiteboard',
            name='files',
            field=models.ManyToManyField(blank=True, default=None, to='whiteboard.File'),
        ),
    ]