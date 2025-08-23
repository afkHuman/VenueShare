from django.contrib import admin
from .models import Venues

# Register your models here.
class VenuesAdmin(admin.ModelAdmin):
    list_display = ('idNumber', 'location', 'address', 'venueType', 'size', 'capacity', 'slug')
    prepopulated_fields = {'slug': ("idNumber", "location")}

admin.site.register(Venues)