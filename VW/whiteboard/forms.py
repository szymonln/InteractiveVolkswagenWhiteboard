from django import forms
from django.forms import ModelForm
from django.db import models
from .models import *


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = ['name', 'area', 'owner', 'whiteboard']


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'whiteboards']


class WhiteboardForm(ModelForm):
    class Meta:
        model = Whiteboard
        fields = []