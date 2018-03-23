from django.shortcuts import render
from project.models import *
from project.forms import BathroomForm
from project.forms import UserForm, UserProfileForm
# Create your views here.


def index(request):
    bathroom_list = Bathroom.objects.values_list('name', 'bathroomSlug',)
    context_dict = {'bathrooms': bathroom_list}
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
        bathroom = Bathroom.objects.all().get(bathroomSlug=bathroomSlug)
        context = {'toilet': bathroom,
                   'interaction': BathroomInteraction.objects.filter(b=bathroom),
                   'rating': bathroom.rating,
                   'images': BathroomImage.objects.filter(bathroom=bathroom)}
    except:
        context = {}
    return render(request, 'project/show_toilet.html', context)


def register(request):
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
            print (user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'project/sign_up.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


