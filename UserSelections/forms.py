from django import forms
from .models import eventingSelection, womens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelection, womens_track_4x100_relaySelection, mens_track_4x100_relaySelection, womens_decathalonSelection, mens_decathalonSelection, womens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelection, womens_swimming_200m_backstrokeSelection, mens_swimming_1500m_freestyleSelection, mens_golfSelection, womens_basketballSelection, womens_soccerSelection, mens_soccerSelection, womens_beach_volleyballSelection, mens_waterpoloSelection, womens_bmxSelection, mens_bmxSelection, mens_handballSelection

class eventingSelectionForm(forms.ModelForm):
    class Meta:
        model = eventingSelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_all_around_gymnasticsSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_all_around_gymnasticsSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_all_around_gymnasticsSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_all_around_gymnasticsSelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_track_4x100_relaySelectionForm(forms.ModelForm):
    class Meta:
        model = womens_track_4x100_relaySelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_track_4x100_relaySelectionForm(forms.ModelForm):
    class Meta:
        model = mens_track_4x100_relaySelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_decathalonSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_decathalonSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_decathalonSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_decathalonSelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_swimming_4x100_medley_relaySelectionForm(forms.ModelForm):
    class Meta:
        model = womens_swimming_4x100_medley_relaySelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_swimming_4x100_medley_relaySelectionForm(forms.ModelForm):
    class Meta:
        model = mens_swimming_4x100_medley_relaySelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_swimming_200m_backstrokeSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_swimming_200m_backstrokeSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_swimming_1500m_freestyleSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_swimming_1500m_freestyleSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_golfSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_golfSelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_basketballSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_basketballSelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_soccerSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_soccerSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_soccerSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_soccerSelection
        fields = ('gold', 'silver', 'bronze')     

class womens_beach_volleyballSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_beach_volleyballSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_waterpoloSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_waterpoloSelection
        fields = ('gold', 'silver', 'bronze')
        
class womens_bmxSelectionForm(forms.ModelForm):
    class Meta:
        model = womens_bmxSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_bmxSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_bmxSelection
        fields = ('gold', 'silver', 'bronze')
        
class mens_handballSelectionForm(forms.ModelForm):
    class Meta:
        model = mens_handballSelection
        fields = ('gold', 'silver', 'bronze')