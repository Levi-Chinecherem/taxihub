from django.shortcuts import render, redirect
from .models import Booking
from taxis.models import Taxi
from django.contrib.auth.decorators import login_required

@login_required
def book_taxi(request):
    if request.method == 'POST':
        taxi_id = request.POST.get('taxi')
        pickup_time = request.POST.get('pickup_time')
        
        # Check if both taxi_id and pickup_time are provided
        if taxi_id and pickup_time:
            taxi = Taxi.objects.get(id=taxi_id)
            if taxi:
                booking = Booking.objects.create(
                    taxi=taxi,
                    pickup_time=pickup_time,
                    user=request.user
                )
                return redirect('view_bookings')

    # Get all available taxis to populate the options in the form
    available_taxis = Taxi.objects.filter(is_available=True)
    return render(request, 'bookings/book_taxi.html', {'available_taxis': available_taxis})

@login_required
def view_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/view_bookings.html', {'bookings': bookings})
