from django import forms
from .models import Ranking

class RankingsForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ('first_name','last_name','email',)