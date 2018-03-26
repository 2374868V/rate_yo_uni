from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg
from project.forms import *
# Create your views here.


def index(request):
    context = {'bathrooms': Bathroom.objects.all()}
    return render(request, 'project/home.html', context)


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
    return render(request, 'project/sign_up.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


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


def show_toilet(request, bSlug):
    context = {}
    try:
        b = Bathroom.objects.get(bSlug=bSlug)
        context['toilet'] = b
        context['rating'] = Rate.objects.filter(bathroom=b).aggregate(Avg('rating'))
        context['comments'] = Comment.objects.filter(bathroom=b)
        return render(request, 'project/toilet.html', context)
    except:
        index(request)


@login_required
def rate(request, bSlug):
    context = {}
    try:
        toilet = Bathroom.objects.get(bSlug=bSlug)
        context['toilet'] = toilet
    except:
        index(request)
    form = RatingForm
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    context['form'] = form
    return render(request, 'project/rate.html', context)


@login_required
def comment(request, bSlug):
    context = {}
    try:
        toilet = Bathroom.objects.get(bSlug=bSlug)
        context['toilet'] = toilet
    except:
        index(request)
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    context['form'] = form
    return render(request, 'project/comment.html', context)

#
# @login_required
# def make_comment(request):
#     form = CommentForm
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#         else:
#             print(form.errors)
#     return render(request, 'project/show_toilet.html')
#
#
# @login_required
# def make_rating(request):
#     bathroom = None
#     user = None
#     r = None
#     if request.method == 'GET':
#         bathroom = request.GET['bathroom']
#         user = request.GET['user']
#         r = request.GET['rating']
#     if bathroom:
#         b = Bathroom.objects.get(bahtroomSlug=bathroom)
#         if user:
#             u = UserProfile.objects.get(userSlug=user)
#
#     return HttpResponse(r)