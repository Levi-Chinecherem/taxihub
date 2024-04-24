from django.contrib import admin
from .models import Taxi
from django.utils.safestring import mark_safe

class TaxiAdmin(admin.ModelAdmin):
    list_display = ('plate_number', 'model', 'is_available', 'display_image')
    list_filter = ('is_available',)
    search_fields = ('plate_number', 'model')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        else:
            return 'No Image'
    display_image.short_description = 'Image Preview'

admin.site.register(Taxi, TaxiAdmin)
