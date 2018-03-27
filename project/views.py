from django.shortcuts import render
from project.models import *
from project.forms import BathroomForm
from django.db.models import Q
from django import forms
# Create your views here.


def index(request):
    bathroom_list = Bathroom.objects.values_list('name', 'bathroomSlug', 'building', 'rating', 'level', 'gender')[0:5]
    searchresponse_list = []


    if request.method == 'GET':

        term = request.GET.get('search_box', None)
        if(term is not None):
            searchresponse_list = Bathroom.objects.all().filter(Q(name__icontains=term) | Q(building__icontains=term)).values_list('name', 'bathroomSlug')


    context_dict = {'bathrooms': bathroom_list, 'searchresponse': searchresponse_list}
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

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=usename, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account is disabled")
        else:
            print("Incorrect username or password")
            return HttpResponse("Invalid login details")
    else:
        return render(request, 'project/login.html', {})
