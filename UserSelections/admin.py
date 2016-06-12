from django.contrib import admin
from .models import UserSelection

class UserSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(UserSelection, UserSelectionAdmin)
