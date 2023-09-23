from django.contrib import admin
from national_cuisine.models import NationalCuisine


@admin.register(NationalCuisine)
class NationalCuisineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
