from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import loader
from django.forms import formset_factory, inlineformset_factory
from django.utils.datastructures import MultiValueDictKeyError

from .models import *
from .forms import AgendaForm, AreaForm, FileFormSet, WhiteboardFormSet, FileForm
from django.shortcuts import redirect
import time
from datetime import datetime
import os


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
            context = {}
            agenda = Agenda(name=data['name'], owner=data['owner'])
            agenda.save()
            request.session['current_agenda_pk'] = agenda.pk
            if data['area'] is not None:
                request.session['current_area_pk'] = data["area"].pk
                return redirect('create_select_whiteboard')
            elif data['area'] is None:
                area_form = AreaForm(request.POST)
                context['back'] = "/"
                context['form'] = area_form
                return redirect('create_area')
    else:
        form = AgendaForm()

    return render(request, 'create_agenda.html', {'form': form})


def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST or None)
        context = dict()
        context['back'] = "/"
        context['form'] = form
        if form.is_valid():
            new_area_data = form.cleaned_data
            area = Area(name=new_area_data['name'], owner=request.user)
            area.save()
            current_agenda_pk = request.session['current_agenda_pk']
            agenda = Agenda.objects.filter(pk=current_agenda_pk)[0]
            agenda.update(area=area)
            request.session['current_area_pk'] = area.pk
            return redirect('create_select_whiteboard')
    else:
        form = AreaForm(request.POST or None)

    return render(request, 'create_area.html', {'form': form})


def create_select_whiteboard(request):
    current_area_pk = request.session['current_area_pk']
    current_agenda_pk = request.session['current_agenda_pk']
    current_area = Area.objects.filter(pk=current_area_pk)[0]
    current_agenda = Agenda.objects.filter(pk=current_agenda_pk)[0]
    if request.method == "POST":
        formset = WhiteboardFormSet(request.POST)
        if formset.is_valid():
            request.session['whiteboards'] = []
            it = 0
            for form in formset:
                data = form.cleaned_data
                whiteboard = Whiteboard(name=data['name'])
                whiteboard.save()
                request.session['whiteboards'].append({})
                request.session['whiteboards'][it]['name'] = data['name']
                request.session['whiteboards'][it]['pk'] = whiteboard.pk
                current_area.whiteboards.add(whiteboard)
                current_agenda.selected_whiteboards.add(whiteboard)
                it += 1
            request.session['whiteboards_count'] = str(it)
            return redirect('add_files_to_whiteboard')
    else:
        formset = WhiteboardFormSet(request.POST or None)

    return render(request, 'create_whiteboards.html', {'formset': formset})


def add_files_to_whiteboard(request):
    whiteboards_count = int(request.session['whiteboards_count'])
    whiteboards_names = []
    for i in range(whiteboards_count):
        name = request.session['whiteboards'][i]['name']
        whiteboards_names.append(name)
    if request.method == "POST":
        formset_dyn = formset_factory(FileForm, extra=whiteboards_count)
        formset = formset_dyn(request.POST, request.FILES)
        formset_names = zip(formset, whiteboards_names)
        if formset.is_valid():
            it = 0
            for form in formset:
                current_whiteboard_pk = request.session['whiteboards'][it]['pk']
                current_whiteboard = Whiteboard.objects.filter(pk=current_whiteboard_pk)[0]
                base_file_name = 'form-'+str(it)+'-file'
                if request.FILES.get(base_file_name):
                    file = request.FILES[base_file_name]
                    file_path = handle_uploaded_file(file, request.user)
                    file_obj = File(date_created=date_now(), path=file_path, file=file_path, owner=request.user, name=file.name)
                    file_obj.save()
                    current_whiteboard.files.add(file_obj)
                else:
                    for i in range(15):
                        try:
                            file = request.FILES[base_file_name+str(i)]
                            file_path = handle_uploaded_file(file, request.user)
                            file_obj = File(date_created=date_now(), file=file_path, owner=request.user, name=file.name)
                            file_obj.save()
                            current_whiteboard.files.add(file_obj)
                        except MultiValueDictKeyError:
                            continue
                it += 1
            return redirect('meeting')
    else:
        formset_dyn = formset_factory(FileForm, extra=whiteboards_count)
        formset = formset_dyn(request.POST or None)
        formset_names = zip(formset, whiteboards_names)

    return render(request, 'add_files_to_whiteboard.html', {'formset': formset_names,
                                                            'management_form': formset.management_form})


def handle_uploaded_file(f, user):
    date = datetime.today().strftime('%Y-%m-%d')
    BASE = os.path.dirname(os.path.abspath(__file__))
    try:
        os.mkdir(os.path.join(BASE, 'documents/' + str(date)))
        os.mkdir(os.path.join(BASE, 'documents/' + str(date) + '/' + str(user)))
    except FileExistsError:
        pass
    upload_path = os.path.join(BASE, 'documents/' + str(date) + '/' + str(user) + '/' + f.name)
    with open(upload_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return 'documents/' + str(date) + '/' + str(user) + '/' + f.name


def meeting(request):
    current_agenda_pk = request.session['current_agenda_pk']
    current_agenda = Agenda.objects.filter(pk=current_agenda_pk)[0]
    whiteboards = request.session['whiteboards']

    context = {}
    context['name'] = current_agenda.name
    whiteboard_o = Whiteboard.objects.filter(pk=whiteboards[0]['pk'])
    files = whiteboard_o[0].files.all()
    context['files'] = []
    for file in files:
        context['files'].append(file.path)

    return render(request, 'meeting.html', context)