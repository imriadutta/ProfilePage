from django.contrib import admin
from service.models import User


class AdminUser(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'dob', 'sex', 'pic')

admin.site.register(User, AdminUser)