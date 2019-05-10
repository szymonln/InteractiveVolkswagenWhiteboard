from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.timezone import now as date_now



class File(models.Model):
    date = datetime.today().strftime('%Y-%m-%d')
    date_created = models.DateTimeField(blank=True, default=date_now())
    name = models.CharField(max_length=100, default=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    file = models.FileField()
    path = models.TextField(null=True)

    def __str__(self):
        return 'File: ' + str(self.name)


class Whiteboard(models.Model):
    name = models.CharField(max_length=100, default=None)
    files = models.ManyToManyField(File, default=None, blank=True)

    def __str__(self):
        return 'Whiteboard: ' + str(self.name)


class Report(models.Model):
    name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return 'Report: ' + str(self.name)


class Area(models.Model):
    name = models.CharField(max_length=100, default=None)
    whiteboards = models.ManyToManyField(Whiteboard, default=None, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return 'Area: ' + str(self.name)


class Agenda(models.Model):
    name = models.CharField(max_length=100, default=None)
    area = models.ForeignKey(Area, default=None, on_delete=models.SET(None), blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    content = models.TextField(blank=True, null=True)
    selected_whiteboards = models.ManyToManyField(Whiteboard, default=None, blank=True, null=True)

    def __str__(self):
        return 'Agenda: ' + str(self.name)


