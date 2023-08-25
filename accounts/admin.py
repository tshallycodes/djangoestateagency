from django.contrib import admin
from .models import Users

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'reg_date')
    list_display_links = ('id', 'fullname')
    list_filter = ('fullname', 'email')
    search_fields = ('fullname',)
    list_per_page = 25

admin.site.register(Users, UsersAdmin)