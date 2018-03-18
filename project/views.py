from django.shortcuts import render
from django.http import HttpResponse
from project.models import Bathroom, BathroomInteraction
# Create your views here.
def index(request):

    bathroom_list = Bathroom.objects.order_by('-rating')
    context_dict = {'bathrooms': bathroom_list}
    return render(request, 'project/home.html', context_dict)

def sign_up(request):
    return render(request, 'project/sign_up.html')

def add_toilet(request):
    return render(request, 'project/add_toilet.html')

def show_toilet(request):
    return render(request, 'project/show_toilet.hmtl')

