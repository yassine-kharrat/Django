from django.contrib import admin
from .models import category

class CategoryAdmin(admin.ModelAdmin):
    search_fields=('title',)

admin.site.register(category, CategoryAdmin)
