from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.forms import CarsForm
from app.models import Cars

def home(request):
  data = {}
  data['db'] = Cars.objects.all()
  return render(request, 'index.html', data)

def createform(request):
  data = {}
  data['form'] = CarsForm()
  return render(request, 'form.html', data)

def create(request):
  form = CarsForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('home')
  
def view(request, pk):
  data = {}
  data['db'] = Cars.objects.get(pk=pk)
  return render(request, 'view.html', data)