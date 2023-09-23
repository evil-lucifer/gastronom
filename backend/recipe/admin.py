from django.contrib import admin
from recipe.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'national_cuisine')
    list_display_links = ('id', 'name', 'category', 'national_cuisine')
