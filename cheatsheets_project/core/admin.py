from django.contrib import admin
from .models import Technology, CheatSheet

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CheatSheet)
class CheatSheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'type', 'created_at')
    list_filter = ('technology', 'type', 'created_at')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
