from django.contrib import admin
from .models import Sport, Country, Athlete

class SportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"sport_slug": ("sport_name",)}

admin.site.register(Sport, SportAdmin)
admin.site.register(Country)
admin.site.register(Athlete)
