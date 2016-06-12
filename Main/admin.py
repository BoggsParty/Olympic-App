from django.contrib import admin
from .models import PasswordReset, LostUserName

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date',)
admin.site.register(PasswordReset, PasswordResetAdmin)

class LostUserNameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date',)
admin.site.register(LostUserName, LostUserNameAdmin)
