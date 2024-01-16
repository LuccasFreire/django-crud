from django.shortcuts import render
from django.http import HttpResponse
from app.forms import CarsForm

def home(request):
  return render(request, 'index.html')

def create(request):
  data = {}
  data['form'] = CarsForm()
  return render(request, 'form.html', data)