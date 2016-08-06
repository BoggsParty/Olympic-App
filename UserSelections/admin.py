from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import eventingSelection, eventingOptions, womens_all_around_gymnasticsSelection, womens_all_around_gymnasticsOptions, mens_all_around_gymnasticsSelection, mens_all_around_gymnasticsOptions, womens_track_4x100_relaySelection, womens_track_4x100_relayOptions, mens_track_4x100_relaySelection, mens_track_4x100_relayOptions, womens_decathalonSelection, womens_decathalonOptions, mens_decathalonSelection, mens_decathalonOptions, womens_swimming_4x100_medley_relaySelection, womens_swimming_4x100_medley_relayOptions, mens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relayOptions, womens_swimming_200m_backstrokeSelection, womens_swimming_200m_backstrokeOptions, mens_swimming_1500m_freestyleSelection, mens_swimming_1500m_freestyleOptions, mens_golfSelection, mens_golfOptions, womens_basketballSelection, womens_basketballOptions, womens_soccerSelection, womens_soccerOptions, mens_soccerSelection, mens_soccerOptions, womens_beach_volleyballSelection, womens_beach_volleyballOptions, mens_waterpoloSelection, mens_waterpoloOptions, womens_bmxSelection, womens_bmxOptions, mens_bmxSelection, mens_bmxOptions, mens_handballSelection, mens_handballOptions, show_jumpingSelection, show_jumpingOptions

# Selection model admin-----------------------------------------
class eventingSelectionResource(resources.ModelResource):
    class Meta:
        model = eventingSelection     
class eventingSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(eventingSelection, eventingSelectionAdmin)

class womens_all_around_gymnasticsSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_all_around_gymnasticsSelection, womens_all_around_gymnasticsSelectionAdmin)

class mens_all_around_gymnasticsSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelectionAdmin)

class womens_track_4x100_relaySelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_track_4x100_relaySelection, womens_track_4x100_relaySelectionAdmin)

class mens_track_4x100_relaySelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_track_4x100_relaySelection, mens_track_4x100_relaySelectionAdmin)

class womens_decathalonSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_decathalonSelection, womens_decathalonSelectionAdmin)

class mens_decathalonSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_decathalonSelection, mens_decathalonSelectionAdmin)

class womens_swimming_4x100_medley_relaySelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_swimming_4x100_medley_relaySelection, womens_swimming_4x100_medley_relaySelectionAdmin)

class mens_swimming_4x100_medley_relaySelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelectionAdmin)

class womens_swimming_200m_backstrokeSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_swimming_200m_backstrokeSelection, womens_swimming_200m_backstrokeSelectionAdmin)

class mens_swimming_1500m_freestyleSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_swimming_1500m_freestyleSelection, mens_swimming_1500m_freestyleSelectionAdmin)

class mens_golfSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_golfSelection, mens_golfSelectionAdmin)

class womens_basketballSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_basketballSelection, womens_basketballSelectionAdmin)

class womens_soccerSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_soccerSelection, womens_soccerSelectionAdmin)

class mens_soccerSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_soccerSelection, mens_soccerSelectionAdmin)

class womens_beach_volleyballSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_beach_volleyballSelection, womens_beach_volleyballSelectionAdmin)

class mens_waterpoloSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_waterpoloSelection, mens_waterpoloSelectionAdmin)

class womens_bmxSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(womens_bmxSelection, womens_bmxSelectionAdmin)

class mens_bmxSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_bmxSelection, mens_bmxSelectionAdmin)

class mens_handballSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(mens_handballSelection, mens_handballSelectionAdmin)

class show_jumpingSelectionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('user', 'sport_name','date_created',)
    ordering = ('user','-date_created',)
    pass
admin.site.register(show_jumpingSelection, show_jumpingSelectionAdmin)


#Options Model Admin--------------------------------------------

class eventingOptionsResource(resources.ModelResource):
    class Meta:
        model = eventingOptions        
class eventingOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(eventingOptions, eventingOptionsAdmin)

class womens_all_around_gymnasticsOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_all_around_gymnasticsOptions       
class womens_all_around_gymnasticsOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_all_around_gymnasticsOptions, womens_all_around_gymnasticsOptionsAdmin)


class mens_all_around_gymnasticsOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_all_around_gymnasticsOptions       
class mens_all_around_gymnasticsOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_all_around_gymnasticsOptions, mens_all_around_gymnasticsOptionsAdmin)


class womens_track_4x100_relayOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_track_4x100_relayOptions       
class womens_track_4x100_relayOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_track_4x100_relayOptions, womens_track_4x100_relayOptionsAdmin)


class mens_track_4x100_relayOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_track_4x100_relayOptions       
class mens_track_4x100_relayOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_track_4x100_relayOptions, mens_track_4x100_relayOptionsAdmin)


class womens_decathalonOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_decathalonOptions       
class womens_decathalonOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_decathalonOptions, womens_decathalonOptionsAdmin)


class mens_decathalonOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_decathalonOptions       
class mens_decathalonOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_decathalonOptions, mens_decathalonOptionsAdmin)


class womens_swimming_4x100_medley_relayOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_swimming_4x100_medley_relayOptions       
class womens_swimming_4x100_medley_relayOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_swimming_4x100_medley_relayOptions, womens_swimming_4x100_medley_relayOptionsAdmin)


class mens_swimming_4x100_medley_relayOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_swimming_4x100_medley_relayOptions       
class mens_swimming_4x100_medley_relayOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_swimming_4x100_medley_relayOptions, mens_swimming_4x100_medley_relayOptionsAdmin)


class womens_swimming_200m_backstrokeOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_swimming_200m_backstrokeOptions       
class womens_swimming_200m_backstrokeOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_swimming_200m_backstrokeOptions, womens_swimming_200m_backstrokeOptionsAdmin)


class mens_swimming_1500m_freestyleOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_swimming_1500m_freestyleOptions       
class mens_swimming_1500m_freestyleOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_swimming_1500m_freestyleOptions, mens_swimming_1500m_freestyleOptionsAdmin)


class mens_golfOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_golfOptions       
class mens_golfOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_golfOptions, mens_golfOptionsAdmin)


class womens_basketballOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_basketballOptions       
class womens_basketballOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_basketballOptions, womens_basketballOptionsAdmin)


class womens_soccerOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_soccerOptions       
class womens_soccerOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_soccerOptions, womens_soccerOptionsAdmin)


class mens_soccerOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_soccerOptions       
class mens_soccerOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_soccerOptions, mens_soccerOptionsAdmin)


class womens_beach_volleyballOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_beach_volleyballOptions       
class womens_beach_volleyballOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_beach_volleyballOptions, womens_beach_volleyballOptionsAdmin)


class mens_waterpoloOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_waterpoloOptions       
class mens_waterpoloOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_waterpoloOptions, mens_waterpoloOptionsAdmin)


class womens_bmxOptionsResource(resources.ModelResource):
    class Meta:
        model = womens_bmxOptions       
class womens_bmxOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(womens_bmxOptions, womens_bmxOptionsAdmin)


class mens_bmxOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_bmxOptions       
class mens_bmxOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_bmxOptions, mens_bmxOptionsAdmin)


class mens_handballOptionsResource(resources.ModelResource):
    class Meta:
        model = mens_handballOptions       
class mens_handballOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(mens_handballOptions, mens_handballOptionsAdmin)


class show_jumpingOptionsResource(resources.ModelResource):
    class Meta:
        model = show_jumpingOptions       
class show_jumpingOptionsAdmin(ImportExportModelAdmin):
    pass
admin.site.register(show_jumpingOptions, show_jumpingOptionsAdmin)