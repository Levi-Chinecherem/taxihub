from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_taxi, name='book_taxi'),
    path('view/', views.view_bookings, name='view_bookings'),
    # Add other booking-related URLs here
]
