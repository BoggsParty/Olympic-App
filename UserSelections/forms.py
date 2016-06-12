from django import forms
from .models import UserSelection

class UserSelectionForm(forms.ModelForm):
    class Meta:
        model = UserSelection
        fields = ('gold_medal_winner','silver_medal_winner','bronze_medal_winner',)
        
class UserFirstSelectionForm(forms.ModelForm):
    class Meta:
        model = UserSelection
        fields =()