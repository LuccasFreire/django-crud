from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from app.forms import CarsForm
from app.models import Cars
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator

def home(request):
  data = {}
  all = Cars.objects.all()
  paginator = Paginator(all,2)
  pages = request.GET.get('page')
  data['db'] = paginator.get_page(pages)
  return render(request, 'index.html', data)

def createform(request):
  data = {}
  data['form'] = CarsForm()
  return render(request, 'form.html', data)

def isajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


#def create(request):
#  form = CarsForm(request.POST or None)
#  if form.is_valid():
#    form.save()
#    return redirect('home')
#  else:
#    print(form.errors.as_data())

def create(request):
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CarsForm()

    return render(request, 'form.html', {'form': form})

def view(request, pk):
  data = {}
  data['db'] = Cars.objects.get(pk=pk)
  return render(request, 'view.html', data)

def edit(request,pk):
  data = {}
  data['db'] = Cars.objects.get(pk=pk)
  data['form'] = CarsForm(instance=data['db'])
  return render(request, 'form.html', data)

def update(request,pk):
  data = {}
  data['db'] = Cars.objects.get(pk=pk)
  form = CarsForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save
  return redirect('home')

def delete(request,pk):
  db = Cars.objects.get(pk=pk)
  db.delete()
  return redirect('home')