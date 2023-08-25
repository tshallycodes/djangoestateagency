from django.contrib import admin
from .models import Properties

# Register your models here.
class PropertiesAdmin(admin.ModelAdmin):
    list_display = ('agent_id', 'name', 'list_date')
    list_display_links = ('agent_id', 'name')
    list_filter = ('name',)
    search_fields = ('agent_id', 'name')
    list_per_page = 25

admin.site.register(Properties, PropertiesAdmin)