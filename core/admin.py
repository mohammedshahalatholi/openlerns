from django.contrib import admin
from .models import Technology, CheatSheet, Category, SiteConfiguration

@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # Prevent creating multiple instances if one exists
        if SiteConfiguration.objects.exists():
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Prevent deleting the configuration
        return False

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'cheatsheet_count')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')

    def cheatsheet_count(self, obj):
        return obj.cheatsheets.count()
    cheatsheet_count.short_description = 'CheatSheets'

@admin.register(CheatSheet)
class CheatSheetAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'file_type', 'created_at')
    list_filter = ('technology', 'file_type', 'created_at')
    search_fields = ('title', 'technology__name')
    prepopulated_fields = {'slug': ('title',)}
