from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import conference
from users.models import reservation
from django.db.models import Count
class ReservatinInLine(admin.TabularInline):
    model = reservation
    extra = 1
    readonly_fields = ('reservation_date',)
    can_delete = False

class ParticipantFilter(admin.SimpleListFilter):
    title="participant filter"
    parameter_name="participants"
    def lookups(self, request: Any, model_admin: Any):
        return (
            ('0',('No participants')),
            ('more',('More participants'))
        )
    def queryset(self, request, queryset):
        if self.value()=='0':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count=0)
        if self.value() == 'more':
            return queryset.annotate(participant_count=Count('reservations')).filter(participant_count__gt=0)
        return queryset


class ConferenceAdmin(admin.ModelAdmin):
    list_display=('title','location','start_date','end_date','price')
    search_fields=('title',)
    list_per_page=2
    ordering=('start_date','title')
    list_filter = ['category', 'start_date', ParticipantFilter]
    fieldsets=(
        ('description',{
            'fields':('title','description','category','location')
        }),
        ('horaires',{
            'fields':('start_date','end_date')
        }),
        ('documents',{
            'fields':('program',)
        })
    )
    #readonly_fields=('created_at','updated_at')
    inlines=[ReservatinInLine]
    autocomplete_fields=['category']
admin.site.register(conference,ConferenceAdmin)
