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
        #gender = request.GET.get('select_gender', None)

        if(term is not None and sort is not None):
            bathroom_list = Bathroom.objects.all().filter(
                Q(name__icontains=term) | Q(building__icontains=term)
            ).values_list(
                'name', 'bathroomSlug', 'building', 'rating', 'level', 'gender'
            ).order_by(
                sort
            )


    context_dict = {'bathroom_list': bathroom_list}
    return render(request, 'project/home.html', context_dict)


def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'project/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def add_toilet(request):
    form = BathroomForm
    if request.method == 'POST':
        form = BathroomForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return show_toilet(request, form.cleaned_data['slug'] )
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
