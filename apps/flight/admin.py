from django.contrib import admin
from .models import *

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_c')
    list_display_links = ('id', 'from_c')
    ordering = ('from_c',)