from django import forms
from django.forms import ModelForm, formset_factory
from django.db import models
from .models import *


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        fields = ['name', 'area', 'owner']
        labels = {'name': '', 'area': 'Area', 'owner': 'Owner'}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Agenda Name'
            })
        }


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['name', 'whiteboards']
        labels = {'name': ''}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Area Name'
            })
        }


class WhiteboardForm(ModelForm):
    class Meta:
        model = Whiteboard
        fields = ['name']
        labels = {'name': ''}
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Whiteboard Name'
            }
            )
        }

WhiteboardFormSet = formset_factory(WhiteboardForm, extra=1)


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['file']
        labels = {'file': ''}

FileFormSet = formset_factory(FileForm, extra=1)
