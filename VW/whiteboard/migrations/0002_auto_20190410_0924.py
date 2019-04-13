# Generated by Django 2.2 on 2019-04-10 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whiteboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Whiteboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='area',
            name='file',
        ),
        migrations.AddField(
            model_name='area',
            name='whiteboards',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='whiteboard.Whiteboard'),
        ),
    ]