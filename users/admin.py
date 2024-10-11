from django.contrib import admin
from .models import participant
from .models import reservation

admin.site.register(participant)
admin.site.register(reservation)