from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView
from .models import Finch

# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request,finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request,'finches/detail.html', {'finch':finch})

class FinchCreate(CreateView):
  model = Finch
  fields = '__all__'