from django.shortcuts import render, get_object_or_404, redirect
from .models import Taxi
from .forms import TaxiForm
from .decorators import admin_required 
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'taxis/index.html')

def taxi_list(request):
    taxis = Taxi.objects.all()
    return render(request, 'taxis/taxi_list.html', {'taxis': taxis})

# Add taxi view restricted to admins
@login_required
@admin_required
def add_taxi(request):
    if request.method == 'POST':
        form = TaxiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('taxi_list')
    else:
        form = TaxiForm()
    return render(request, 'taxis/add_taxi.html', {'form': form})

# Edit taxi view restricted to admins
@login_required
@admin_required
def edit_taxi(request, taxi_id):
    taxi = Taxi.objects.get(id=taxi_id)
    if request.method == 'POST':
        form = TaxiForm(request.POST, request.FILES, instance=taxi)
        if form.is_valid():
            form.save()
            return redirect('taxi_list')
    else:
        form = TaxiForm(instance=taxi)
    return render(request, 'taxis/edit_taxi.html', {'form': form, 'taxi': taxi})

@login_required
def taxi_detail(request, taxi_id):
    taxi = get_object_or_404(Taxi, id=taxi_id)
    return render(request, 'taxis/taxi_detail.html', {'taxi': taxi})

def no_permission(request):
    return render(request, 'taxis/no_permission.html')
