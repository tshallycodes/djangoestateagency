from django.contrib import admin
from .models import MyMessages

# Register your models here.
class AdminMessage(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'pname', 'plocation', 'msg_date', 'agent_id')
    list_display_links = ('id', 'email')
    search_fields = ('agent_id', 'name')
    list_filter = ('agent_id',)
    list_per_page = 25

admin.site.register(MyMessages, AdminMessage)
