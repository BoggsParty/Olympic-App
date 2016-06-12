from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from .forms import UserForm, PasswordForm, LostUserNameForm
from Rankings.forms import RankingsForm
from UserSelections.forms import UserFirstSelectionForm
from Rankings.models import Ranking
from django.utils import timezone


@login_required
def dashboard(request):
    user = Ranking.objects.all().order_by('-score')
    return render(request, 'Main/dashboard.html', {'user': user})

@login_required
def adduser(request):    
    if request.method == "POST":
        form = RankingsForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.username = selection.user
            selection.save()
            return redirect('createchoice')
    else:
        form = RankingsForm()
    return render(request, 'Registration/new_user.html', {'form': form})

def reset_password(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.date = timezone.now()
            record.save()
            return redirect ('password_confirmation')
    else:
        form = PasswordForm()
    return render(request, 'registration/password_reset1.html', {'form': form}) 

def password_confirmation(request):
    return render(request, 'registration/password_reset2.html')

def retrieve_username(request):
    if request.method == "POST":
        form = LostUserNameForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.date = timezone.now()
            record.save()
            return redirect ('username_confirmation')
    else:
<<<<<<< HEAD
        form = LostUserNameForm()
    return render(request, 'registration/retrieve_username1.html', {'form': form}) 

def retrieve_username_confirmation(request):
    return render(request, 'registration/retrieve_username2.html')  
    
@login_required
def create_choice_record(request):
    user = Ranking.objects.filter(user=request.user).filter(user=request.user).order_by('-id')[0]
    if request.method == "POST":
        form2 = UserFirstSelectionForm(request.POST)
        if form2.is_valid():
            record = form2.save(commit=False)
            record.user = request.user
            record.sport_name = 'none'
            record.save()
            return redirect ('dashboard')
    else:
        form2 = UserFirstSelectionForm()
    return render(request, 'Registration/new_user2.html', {'form2': form2, 'user':user})
    
@login_required    
def logout_view(request):
    logout(request)
    return redirect('dashboard')


    




=======
        form = UserForm()
    return render(request, 'registration/createaccount.html', {'form': form})
>>>>>>> b8a76a1e70d14218343ebb7c3edb76b73cd5ae71
