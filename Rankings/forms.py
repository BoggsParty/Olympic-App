from django import forms
from .models import Ranking, Comments

class RankingsForm(forms.ModelForm):
    class Meta:
        model = Ranking
        fields = ('first_name','last_name','email',)
        
class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)