from django.contrib import admin
from .models import Ranking, Comments_On, Comments

class RankingAdmin(admin.ModelAdmin):
    list_display = ('user', 'score',)

admin.site.register(Ranking, RankingAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_created')
admin.site.register(Comments, CommentsAdmin)


admin.site.register(Comments_On)