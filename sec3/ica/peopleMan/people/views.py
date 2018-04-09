# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm
from django.views.generic.edit import FormView
from peopleMan.settings import BASE_DIR

# Create your views here.

def people_list (request):
    all_people = Person.objects.all()
    return render(request, 'people/list.html', {'people': all_people})

def add_person (request):
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PersonForm()
    
    return render(request, 'people/add.html', {'form':form})
