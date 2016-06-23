from django import forms
from django.forms import ModelForm, PasswordInput
from .models import PasswordReset, LostUserName, Suggestions
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password',)
        
class PasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordReset
        fields = ('username', 'email',)
        
class LostUserNameForm(forms.ModelForm):
    class Meta:
        model = LostUserName
        fields = ('first_name', 'last_name', 'email',)
        
class SuggestionsForm(forms.ModelForm):
    class Meta:
        model = Suggestions
        fields = ('suggestion',)