from django.shortcuts import render
from project.models import *
from project.forms import BathroomForm
from django.db.models import Q
from django import forms
# Create your views here.


def index(request):
    bathroom_list = Bathroom.objects.values_list('name', 'bathroomSlug', 'building', 'rating', 'level', 'gender')[0:5]




    if request.method == 'GET':

        term = request.GET.get('search_box', None)
        sort = request.GET.get('select_sort', None)


        if(term is not None and sort is not None):
            bathroom_list = Bathroom.objects.all().filter(
                Q(name__icontains=term) | Q(building__icontains=term)
            ).values_list(
                'name', 'bathroomSlug', 'building', 'rating', 'level', 'gender'
            ).order_by(
                sort
            )
        print(sort)
    context_dict = {'bathroom_list': bathroom_list}
    return render(request, 'project/home.html', context_dict)


def sign_up(request):
    return render(request, 'project/sign_up.html')


def add_toilet(request):
    form = BathroomForm
    if request.method == 'POST':
        form = BathroomForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'project/add_toilet.html', {'form': form})


def show_toilet(request, bathroomSlug):
    try:
        context = {'toilet': Bathroom.objects.all().get(bathroomSlug=bathroomSlug)}
    except:
        context = {}
    return render(request, 'project/show_toilet.html', context)

