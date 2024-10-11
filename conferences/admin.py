from django.contrib import admin
from .models import conference

class ConferenceAdmin(admin.ModelAdmin): 
    list_display=('title', 'location', 'start_date', 'end_date', 'price')
    search_fields=('title',)
    list_per_page=2
admin.site.register(conference,ConferenceAdmin)