from django.contrib import admin
from .models import PasswordReset, LostUserName, Suggestions

class PasswordResetAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date',)
admin.site.register(PasswordReset, PasswordResetAdmin)

class LostUserNameAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date',)
admin.site.register(LostUserName, LostUserNameAdmin)

class SuggestionsAdmin(admin.ModelAdmin):
    list_display = ('suggestion',)
admin.site.register(Suggestions, SuggestionsAdmin)
