from django.contrib import admin
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'taxi', 'pickup_time', 'status']
    list_filter = ['status']
    search_fields = ['user__username', 'taxi__plate_number', 'pickup_time']

admin.site.register(Booking, BookingAdmin)
