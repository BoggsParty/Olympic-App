from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.template import RequestContext
from django.contrib.auth.models import User
from .forms import UserForm, PasswordForm, LostUserNameForm, SuggestionsForm
from Rankings.forms import RankingsForm
from UserSelections.models import eventingSelection, womens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelection, womens_track_4x100_relaySelection, mens_track_4x100_relaySelection, womens_decathalonSelection, mens_decathalonSelection, womens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelection, womens_swimming_200m_backstrokeSelection, mens_swimming_1500m_freestyleSelection, mens_golfSelection, womens_basketballSelection, womens_soccerSelection, mens_soccerSelection, womens_beach_volleyballSelection, mens_waterpoloSelection, womens_bmxSelection, mens_bmxSelection, mens_handballSelection, show_jumpingSelection
from Rankings.models import Ranking
from CountryInfo.models import Sport
from django.utils import timezone
import datetime
from django.db.models import Q


@login_required
def view_all(request):
    eventing = eventingSelection.objects.filter(Q(sport_name='eventing') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_all_around_gymnastics = womens_all_around_gymnasticsSelection.objects.filter(Q(sport_name='womens-all-around-gymnastics') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_all_around_gymnastics = mens_all_around_gymnasticsSelection.objects.filter(Q(sport_name='mens-all-around-gymnastics') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_track_4x100_relay = womens_track_4x100_relaySelection.objects.filter(Q(sport_name='womens-track-4x100-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_track_4x100_relay = mens_track_4x100_relaySelection.objects.filter(Q(sport_name='mens-track-4x100-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_decathalon = womens_decathalonSelection.objects.filter(Q(sport_name='womens-3000m-steeplechase') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_decathalon = mens_decathalonSelection.objects.filter(Q(sport_name='mens-3000m-steeplechase') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_swimming_4x100_medley_relay = womens_swimming_4x100_medley_relaySelection.objects.filter(Q(sport_name='womens-swimming-4x100-medley-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_swimming_4x100_medley_relay = mens_swimming_4x100_medley_relaySelection.objects.filter(Q(sport_name='mens-swimming-4x100-medley-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_swimming_200m_backstroke = womens_swimming_200m_backstrokeSelection.objects.filter(Q(sport_name='womens-swimming-200m-backstroke') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_swimming_1500m_freestyle = mens_swimming_1500m_freestyleSelection.objects.filter(Q(sport_name='mens-swimming-200m-im') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_golf = mens_golfSelection.objects.filter(Q(sport_name='mens-golf') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_soccer = womens_soccerSelection.objects.filter(Q(sport_name='womens-soccer') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_soccer = mens_soccerSelection.objects.filter(Q(sport_name='mens-soccer') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).order_by('-id')[0]
    womens_beach_volleyball = womens_beach_volleyballSelection.objects.filter(Q(sport_name='womens-beach-volleyball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_waterpolo = mens_waterpoloSelection.objects.filter(Q(sport_name='mens-waterpolo') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_bmx = womens_bmxSelection.objects.filter(Q(sport_name='womens-bmx') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_bmx = mens_bmxSelection.objects.filter(Q(sport_name='mens-bmx') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    mens_handball = mens_handballSelection.objects.filter(Q(sport_name='mens-handball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    womens_basketball = womens_basketballSelection.objects.filter(Q(sport_name='womens-basketball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    show_jumping = show_jumpingSelection.objects.filter(Q(sport_name='show-jumping') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'Main/viewall.html', {'eventing':eventing, 'womens_all_around_gymnastics':womens_all_around_gymnastics, 'mens_all_around_gymnastics':mens_all_around_gymnastics, 'womens_track_4x100_relay':womens_track_4x100_relay, 'mens_track_4x100_relay':mens_track_4x100_relay, 'womens_decathalon':womens_decathalon, 'mens_decathalon':mens_decathalon, 'womens_swimming_4x100_medley_relay':womens_swimming_4x100_medley_relay, 'mens_swimming_4x100_medley_relay':mens_swimming_4x100_medley_relay, 'womens_swimming_200m_backstroke':womens_swimming_200m_backstroke, 'mens_swimming_1500m_freestyle':mens_swimming_1500m_freestyle, 'mens_golf':mens_golf, 'womens_basketball':womens_basketball, 'womens_soccer':womens_soccer, 'mens_soccer':mens_soccer, 'womens_beach_volleyball':womens_beach_volleyball, 'mens_waterpolo':mens_waterpolo, 'womens_bmx':womens_bmx, 'mens_bmx':mens_bmx, 'mens_handball':mens_handball, 'show_jumping':show_jumping,})

@login_required
def view_all_1(request):
    now = datetime.datetime.now()
    allow_change = True
    if 32 < now.day:
        allow_change = False
    elif 32 == now.day and 24 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True
    eventing = eventingSelection.objects.filter(sport_name='eventing').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall1.html', {'eventing':eventing, 'allow_change':allow_change,})

@login_required
def view_all_2(request):
    show_jumping = show_jumpingSelection.objects.filter(sport_name='show-jumping').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall2.html', {'show_jumping':show_jumping})
    
@login_required
def view_all_3(request):
    womens_beach_volleyball = womens_beach_volleyballSelection.objects.filter(sport_name='womens-beach-volleyball').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall3.html', {'womens_beach_volleyball':womens_beach_volleyball})
  
@login_required
def view_all_4(request):
    mens_waterpolo = mens_waterpoloSelection.objects.filter(sport_name='mens-waterpolo').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall4.html', {'mens_waterpolo':mens_waterpolo})
    
@login_required
def view_all_5(request):
    womens_bmx = womens_bmxSelection.objects.filter(sport_name='womens-bmx').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall5.html', {'womens_bmx':womens_bmx})
    
@login_required
def view_all_6(request):
    mens_bmx = mens_bmxSelection.objects.filter(sport_name='mens-bmx').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall6.html', {'mens_bmx':mens_bmx})
    
@login_required
def view_all_7(request):
    womens_basketball = womens_basketballSelection.objects.filter(sport_name='womens-basketball').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall7.html', {'womens_basketball':womens_basketball})
    
@login_required
def view_all_8(request):
    mens_handball = mens_handballSelection.objects.filter(sport_name='mens_handball').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall8.html', {'mens_handball':mens_handball})
    
@login_required
def view_all_9(request):
    womens_swimming_4x100_medley_relay = womens_swimming_4x100_medley_relaySelection.objects.filter(sport_name='womens-4x100-medley-relay').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall9.html', {'womens_swimming_4x100_medley_relay':womens_swimming_4x100_medley_relay})
    
@login_required
def view_all_10(request):
    mens_swimming_4x100_medley_relay = mens_swimming_4x100_medley_relaySelection.objects.filter(sport_name='mens-swimming-4x100-medley-relay').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall10.html', {'mens_swimming_4x100_medley_relay':mens_swimming_4x100_medley_relay})
    
@login_required
def view_all_11(request):
    womens_swimming_200m_backstroke = womens_swimming_200m_backstrokeSelection.objects.filter(sport_name='womens-swimming-200m-backstroke').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall11.html', {'womens_swimming_200m_backstroke':womens_swimming_200m_backstroke})

@login_required
def view_all_12(request):
    mens_swimming_1500m_freestyle = mens_swimming_1500m_freestyleSelection.objects.filter(sport_name='mens-swimming-200m-im').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall12.html', {'mens_swimming_1500m_freestyle':mens_swimming_1500m_freestyle})
    
@login_required
def view_all_13(request):
    womens_decathalon = womens_decathalonSelection.objects.filter(sport_name='womens-decathalon').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall13.html', {'womens_decathalon':womens_decathalon})
    
@login_required
def view_all_14(request):
    mens_decathalon = mens_decathalonSelection.objects.filter(sport_name='mens-decathalon').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall14.html', {'mens_decathalon':mens_decathalon})
    
@login_required
def view_all_15(request):
    womens_track_4x100_relay = womens_track_4x100_relaySelection.objects.filter(sport_name='womens-track-4x100-relay').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall15.html', {'womens_track_4x100_relay':womens_track_4x100_relay})
    
@login_required
def view_all_16(request):
    mens_track_4x100_relay = mens_track_4x100_relaySelection.objects.filter(sport_name='mens-track-4x100-relay').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall16.html', {'mens_track_4x100_relay':mens_track_4x100_relay})
    
@login_required
def view_all_17(request):
    womens_soccer = womens_soccerSelection.objects.filter(sport_name='womens-soccer').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall17.html', {'womens_soccer':womens_soccer})
    
@login_required
def view_all_18(request):
    mens_soccer = mens_soccerSelection.objects.filter(sport_name='mens-soccer').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall18.html', {'mens_soccer':mens_soccer})
    
@login_required
def view_all_19(request):
    womens_all_around_gymnastics = womens_all_around_gymnasticsSelection.objects.filter(sport_name='womens-all-around-gymnastics').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall19.html', {'womens_all_around_gymnastics':womens_all_around_gymnastics})

@login_required
def view_all_20(request):
    mens_all_around_gymnastics = mens_all_around_gymnasticsSelection.objects.filter(sport_name='mens-all-around-gymnastics').exclude(user__isnull=True)
    return render(request, 'Main/sportsviewall/viewall20.html', {'mens_all_around_gymnastics':mens_all_around_gymnastics})

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


