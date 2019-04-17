from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from .models import *
from .forms import AgendaForm, AreaForm


def before_meeting(request):
    agendas = Agenda.objects.filter(owner=request.user)
    context = {
        'agendas': agendas,
        'user_name': request.user.get_full_name()
    }
    if request.POST:
        context['areas'] = request.body

    return render(request, 'before_meeting.html', context)


def create_agenda(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AgendaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            agenda = Agenda(name=data['name'], area=data['area'], owner=data['owner'], content=data['whiteboard'])
            agenda.save()
            context = {
                'current_agenda_id': agenda.id
            }
            if data['whiteboard'] is not None and data['area'] is not None:
                context['agenda'] = agenda.id
                return HttpResponse("Created Agenda! " + str(agenda.id))
            elif data['whiteboard'] is None and data['area'] is None:
                return HttpResponse("Need to create whiteboard and area")
            elif data['whiteboard'] is None:
                return HttpResponse("Need to create whiteboard")
            elif data['area'] is None:
                area_form = AreaForm(request.POST)
                context['back'] = "/create_agenda"
                context['form'] = area_form
                return render(request, 'create_area.html', context)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = AgendaForm()

    return render(request, 'create_agenda.html', {'form': form})