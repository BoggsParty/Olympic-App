from django.contrib import admin
from .models import eventingSelection, eventingOptions, womens_all_around_gymnasticsSelection, womens_all_around_gymnasticsOptions, mens_all_around_gymnasticsSelection, mens_all_around_gymnasticsOptions, womens_track_4x100_relaySelection, womens_track_4x100_relayOptions, mens_track_4x100_relaySelection, mens_track_4x100_relayOptions, womens_decathalonSelection, womens_decathalonOptions, mens_decathalonSelection, mens_decathalonOptions, womens_swimming_4x100_medley_relaySelection, womens_swimming_4x100_medley_relayOptions, mens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relayOptions, womens_swimming_200m_backstrokeSelection, womens_swimming_200m_backstrokeOptions, mens_swimming_1500m_freestyleSelection, mens_swimming_1500m_freestyleOptions, mens_golfSelection, mens_golfOptions, womens_basketballSelection, womens_basketballOptions, womens_soccerSelection, womens_soccerOptions, mens_soccerSelection, mens_soccerOptions, womens_beach_volleyballSelection, womens_beach_volleyballOptions, mens_waterpoloSelection, mens_waterpoloOptions, womens_bmxSelection, womens_bmxOptions, mens_bmxSelection, mens_bmxOptions, mens_handballSelection, mens_handballOptions, show_jumpingSelection, show_jumpingOptions

class eventingSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(eventingSelection, eventingSelectionAdmin)

admin.site.register(eventingOptions)

class womens_all_around_gymnasticsSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_all_around_gymnasticsSelection, womens_all_around_gymnasticsSelectionAdmin)

admin.site.register(womens_all_around_gymnasticsOptions)

class mens_all_around_gymnasticsSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelectionAdmin)

admin.site.register(mens_all_around_gymnasticsOptions)

class womens_track_4x100_relaySelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_track_4x100_relaySelection, womens_track_4x100_relaySelectionAdmin)

admin.site.register(womens_track_4x100_relayOptions)

class mens_track_4x100_relaySelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_track_4x100_relaySelection, mens_track_4x100_relaySelectionAdmin)

admin.site.register(mens_track_4x100_relayOptions)

class womens_decathalonSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_decathalonSelection, womens_decathalonSelectionAdmin)

admin.site.register(womens_decathalonOptions)

class mens_decathalonSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_decathalonSelection, mens_decathalonSelectionAdmin)

admin.site.register(mens_decathalonOptions)

class womens_swimming_4x100_medley_relaySelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_swimming_4x100_medley_relaySelection, womens_swimming_4x100_medley_relaySelectionAdmin)

admin.site.register(womens_swimming_4x100_medley_relayOptions)

class mens_swimming_4x100_medley_relaySelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelectionAdmin)

admin.site.register(mens_swimming_4x100_medley_relayOptions)

class womens_swimming_200m_backstrokeSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_swimming_200m_backstrokeSelection, womens_swimming_200m_backstrokeSelectionAdmin)

admin.site.register(womens_swimming_200m_backstrokeOptions)

class mens_swimming_1500m_freestyleSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_swimming_1500m_freestyleSelection, mens_swimming_1500m_freestyleSelectionAdmin)

admin.site.register(mens_swimming_1500m_freestyleOptions)

class mens_golfSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_golfSelection, mens_golfSelectionAdmin)

admin.site.register(mens_golfOptions)

class womens_basketballSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_basketballSelection, womens_basketballSelectionAdmin)

admin.site.register(womens_basketballOptions)

class womens_soccerSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_soccerSelection, womens_soccerSelectionAdmin)

admin.site.register(womens_soccerOptions)

class mens_soccerSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_soccerSelection, mens_soccerSelectionAdmin)

admin.site.register(mens_soccerOptions)

class womens_beach_volleyballSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_beach_volleyballSelection, womens_beach_volleyballSelectionAdmin)

admin.site.register(womens_beach_volleyballOptions)

class mens_waterpoloSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_waterpoloSelection, mens_waterpoloSelectionAdmin)

admin.site.register(mens_waterpoloOptions)

class womens_bmxSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(womens_bmxSelection, womens_bmxSelectionAdmin)

admin.site.register(womens_bmxOptions)

class mens_bmxSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_bmxSelection, mens_bmxSelectionAdmin)

admin.site.register(mens_bmxOptions)

class mens_handballSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(mens_handballSelection, mens_handballSelectionAdmin)

admin.site.register(mens_handballOptions)

class show_jumpingSelectionAdmin(admin.ModelAdmin):
    list_display = ('user', 'sport_name',)
admin.site.register(show_jumpingSelection, show_jumpingSelectionAdmin)

admin.site.register(show_jumpingOptions)