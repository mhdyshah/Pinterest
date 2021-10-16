from django.contrib import admin
from django.contrib.auth.models import Group

from authentication.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'fullname', 'created_at']
    list_filter = ('username', 'email', 'fullname',
                   'created_at', 'updated_at')

    search_fields = ('username', 'email', 'fullname', 'id')
    ordering = ('username', 'email', 'created_at', 'updated_at', 'id')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
