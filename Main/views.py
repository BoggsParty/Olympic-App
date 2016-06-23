from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from .forms import UserForm, PasswordForm, LostUserNameForm, SuggestionsForm
from Rankings.forms import RankingsForm
from UserSelections.models import eventingSelection, womens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelection, womens_track_4x100_relaySelection, mens_track_4x100_relaySelection, womens_decathalonSelection, mens_decathalonSelection, womens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelection, womens_swimming_200m_backstrokeSelection, mens_swimming_1500m_freestyleSelection, mens_golfSelection, womens_basketballSelection, womens_soccerSelection, mens_soccerSelection, womens_beach_volleyballSelection, mens_waterpoloSelection, womens_bmxSelection, mens_bmxSelection, mens_handballSelection
from Rankings.models import Ranking
from CountryInfo.models import Sport
from django.utils import timezone
from django.db.models import Q


@login_required
def view_all(request):
    eventing = eventingSelection.objects.filter(Q(sport_name='eventing') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_all_around_gymnastics = womens_all_around_gymnasticsSelection.objects.filter(Q(sport_name='womens-all-around-gymnastics') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_all_around_gymnastics = mens_all_around_gymnasticsSelection.objects.filter(Q(sport_name='mens-all-around-gymnastics') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_track_4x100_relay = womens_track_4x100_relaySelection.objects.filter(Q(sport_name='womens-track-4x100-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_track_4x100_relay = mens_track_4x100_relaySelection.objects.filter(Q(sport_name='mens-track-4x100-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_decathalon = womens_decathalonSelection.objects.filter(Q(sport_name='womens-decathalon') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_decathalon = mens_decathalonSelection.objects.filter(Q(sport_name='mens-decathalon') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_swimming_4x100_medley_relay = womens_swimming_4x100_medley_relaySelection.objects.filter(Q(sport_name='womens-swimming-4x100-medley-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_swimming_4x100_medley_relay = mens_swimming_4x100_medley_relaySelection.objects.filter(Q(sport_name='mens-swimming-4x100-medley-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_swimming_200m_backstroke = womens_swimming_200m_backstrokeSelection.objects.filter(Q(sport_name='womens-swimming-200m-backstroke') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_swimming_1500m_freestyle = mens_swimming_1500m_freestyleSelection.objects.filter(Q(sport_name='mens-swimming-1500m-freestyle') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_golf = mens_golfSelection.objects.filter(Q(sport_name='mens-golf') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_soccer = womens_soccerSelection.objects.filter(Q(sport_name='womens-soccer') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_soccer = mens_soccerSelection.objects.filter(Q(sport_name='mens-soccer') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).order_by('-id')[0]
    womens_beach_volleyball = womens_beach_volleyballSelection.objects.filter(Q(sport_name='womens-beach-volleyball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_waterpolo = mens_waterpoloSelection.objects.filter(Q(sport_name='mens-waterpolo') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_bmx = womens_bmxSelection.objects.filter(Q(sport_name='womens-bmx') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_bmx = mens_bmxSelection.objects.filter(Q(sport_name='mens-bmx') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_handball = mens_handballSelection.objects.filter(Q(sport_name='mens-handball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_basketball = womens_basketballSelection.objects.filter(Q(sport_name='womens-basketball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'Main/viewall.html', {'eventing':eventing, 'womens_all_around_gymnastics':womens_all_around_gymnastics, 'mens_all_around_gymnastics':mens_all_around_gymnastics, 'womens_track_4x100_relay':womens_track_4x100_relay, 'mens_track_4x100_relay':mens_track_4x100_relay, 'womens_decathalon':womens_decathalon, 'mens_decathalon':mens_decathalon, 'womens_swimming_4x100_medley_relay':womens_swimming_4x100_medley_relay, 'mens_swimming_4x100_medley_relay':mens_swimming_4x100_medley_relay, 'womens_swimming_200m_backstroke':womens_swimming_200m_backstroke, 'mens_swimming_1500m_freestyle':mens_swimming_1500m_freestyle, 'mens_golf':mens_golf, 'womens_basketball':womens_basketball, 'womens_soccer':womens_soccer, 'mens_soccer':mens_soccer, 'womens_beach_volleyball':womens_beach_volleyball, 'mens_waterpolo':mens_waterpolo, 'womens_bmx':womens_bmx, 'mens_bmx':mens_bmx, 'mens_handball':mens_handball,})

@login_required
def view_all_1(request):
    eventing = eventingSelection.objects.filter(sport_name='eventing')
    return render(request, 'Main/sportsviewall/viewall1.html', {'eventing':eventing})

 
@login_required
def dashboard(request):
    user = Ranking.objects.all().order_by('-score')
    sport = Sport.objects.order_by('order')
    return render(request, 'Main/dashboard.html', {'user': user, 'sport': sport})

@login_required
def adduser(request):    
    if request.method == "POST":
        form = RankingsForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.username = selection.user
            selection.save()
            return redirect('about')
    else:
        form = RankingsForm()
    return render(request, 'registration/new_user.html', {'form': form})

@login_required
def about(request):
    if request.method == "POST":
        form = SuggestionsForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.user = request.user
            suggestion.save()
            return redirect ('dashboard')
    else:
        form = SuggestionsForm()
    return render (request, 'Main/about.html', {'form':form})
    
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
    return render(request, 'registration/create_account_success.html')

def retrieve_username(request):
    if request.method == "POST":
        form = LostUserNameForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.date = timezone.now()
            record.save()
            return redirect ('username_confirmation')
    else:
        form = LostUserNameForm()
    return render(request, 'registration/retrieve_username1.html', {'form': form}) 

def retrieve_username_confirmation(request):
    return render(request, 'registration/retrieve_username2.html')  

def create_account_success(request):
    return render(request, 'registration/create_account_success.html')    

@login_required
def account_settings(request):
        return render(request, 'registration/account-settings.html')


#def create_choice_record(request):
   # user = Ranking.objects.filter(user=request.user).filter(user=request.user).order_by('-id')[0]
   # if request.method == "POST":
   #     form2 = UserFirstSelectionForm(request.POST)
   #     if form2.is_valid():
    #        record = form2.save(commit=False)
    #        record.user = request.user
     #       record.sport_name = 'none'
     #       record.save()
     #       return redirect ('dashboard')
   # else:
  #      form2 = UserFirstSelectionForm()
   # return render(request, 'registration/new_user2.html', {'form2': form2, 'user':user})
    
@login_required    
def logout_view(request):
    logout(request)
    return redirect('dashboard')


