from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from .models import *


def before_meeting(request):
    agendas = Agenda.objects.filter(owner=request.user)
    context = {
        'agendas': agendas,
    }
    if request.POST:
        context['areas'] = request.body

    return render(request, 'before_meeting.html', context)
