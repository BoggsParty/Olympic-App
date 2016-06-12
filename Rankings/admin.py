from django.contrib import admin
from .models import Ranking

class RankingAdmin(admin.ModelAdmin):
    list_display = ('user', 'score',)

admin.site.register(Ranking, RankingAdmin)