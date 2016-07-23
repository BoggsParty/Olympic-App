from django.shortcuts import get_object_or_404, render, redirect
from .models import eventingSelection, womens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelection, womens_track_4x100_relaySelection, mens_track_4x100_relaySelection, womens_decathalonSelection, mens_decathalonSelection, womens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelection, womens_swimming_200m_backstrokeSelection, mens_swimming_1500m_freestyleSelection, mens_golfSelection, womens_basketballSelection, womens_soccerSelection, mens_soccerSelection, womens_beach_volleyballSelection, mens_waterpoloSelection, womens_bmxSelection, mens_bmxSelection, mens_handballSelection, show_jumpingSelection
from CountryInfo.models import Sport
from .forms import eventingSelectionForm, womens_all_around_gymnasticsSelectionForm, mens_all_around_gymnasticsSelectionForm, womens_track_4x100_relaySelectionForm, mens_track_4x100_relaySelectionForm, womens_decathalonSelectionForm, mens_decathalonSelectionForm, womens_swimming_4x100_medley_relaySelectionForm, mens_swimming_4x100_medley_relaySelectionForm, womens_swimming_200m_backstrokeSelectionForm, mens_swimming_1500m_freestyleSelectionForm, mens_golfSelectionForm, womens_basketballSelectionForm, womens_soccerSelectionForm, mens_soccerSelectionForm, womens_beach_volleyballSelectionForm, mens_waterpoloSelectionForm, womens_bmxSelectionForm, mens_bmxSelectionForm, mens_handballSelectionForm, show_jumpingSelectionForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime


@login_required
def selection_eventing(request):
    userselection = eventingSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='eventing')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 6 < now.day:
        allow_change = False
    elif 6 == now.day:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True   
    if request.method == "POST":
        form = eventingSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/eventing/')

    else:
        form = eventingSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change}) 

@login_required
def selection_womens_all_around_gymnastics(request):
    userselection = womens_all_around_gymnasticsSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-all-around-gymnastics')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 9 < now.day:
        allow_change = False
    elif 9 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_all_around_gymnasticsSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-all-around-gymnastics/')

    else:
        form = womens_all_around_gymnasticsSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_all_around_gymnastics(request):
    userselection = mens_all_around_gymnasticsSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-all-around-gymnastics')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 8 < now.day:
        allow_change = False
    elif 8 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_all_around_gymnasticsSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-all-around-gymnastics/')

    else:
        form = mens_all_around_gymnasticsSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})
    
@login_required
def selection_womens_track_4x100_relay(request):
    userselection = womens_track_4x100_relaySelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-track-4x100-relay')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 19 < now.day:
        allow_change = False
    elif 19 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_track_4x100_relaySelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-track-4x100-relay/')

    else:
        form = womens_track_4x100_relaySelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_track_4x100_relay(request):
    userselection = mens_track_4x100_relaySelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-track-4x100-relay')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 19 < now.day:
        allow_change = False
    elif 19 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_track_4x100_relaySelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-track-4x100-relay/')

    else:
        form = mens_track_4x100_relaySelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_womens_decathalon(request):
    userselection = womens_decathalonSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-3000m-steeplechase')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 15 < now.day:
        allow_change = False
    elif 15 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_decathalonSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-3000m-steeplechase/')

    else:
        form = womens_decathalonSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_decathalon(request):
    userselection = mens_decathalonSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-3000m-steeplechase')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 17 < now.day:
        allow_change = False
    elif 17 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_decathalonSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-3000m-steeplechase/')

    else:
        form = mens_decathalonSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})
    
@login_required
def selection_womens_swimming_4x100_medley_relay(request):
    userselection = womens_swimming_4x100_medley_relaySelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-swimming-4x100-medley-relay')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 7 == now.month:
        allow_change = True
    elif 12 < now.day:
        allow_change = False
    elif 12 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_swimming_4x100_medley_relaySelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-swimming-4x100-medley-relay/')

    else:
        form = womens_swimming_4x100_medley_relaySelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_swimming_4x100_medley_relay(request):
    userselection = mens_swimming_4x100_medley_relaySelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-swimming-4x100-medley-relay')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 12 < now.day:
        allow_change = False
    elif 12 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_swimming_4x100_medley_relaySelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-swimming-4x100-medley-relay/')

    else:
        form = mens_swimming_4x100_medley_relaySelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_womens_swimming_200m_backstroke(request):
    userselection = womens_swimming_200m_backstrokeSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-swimming-200m-backstroke')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 11 < now.day:
        allow_change = False
    elif 11 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_swimming_200m_backstrokeSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-swimming-200m-backstroke/')

    else:
        form = womens_swimming_200m_backstrokeSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required

def selection_mens_swimming_1500m_freestyle(request):
    userselection = mens_swimming_1500m_freestyleSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-swimming-200m-IM')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 10 < now.day:
        allow_change = False
    elif 10 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_swimming_1500m_freestyleSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-swimming-200m-freestyle/')

    else:
        form = mens_swimming_1500m_freestyleSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_golf(request):
    userselection = mens_golfSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-golf')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 32 < now.day:
        allow_change = False
    elif 32 == now.day and 22 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_golfSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-golf/')

    else:
        form = mens_golfSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_womens_basketball(request):
    userselection = womens_basketballSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-basketball')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 16 < now.day:
        allow_change = False
    elif 16 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_basketballSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-basketball/')

    else:
        form = womens_basketballSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_womens_soccer(request):
    userselection = womens_soccerSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-soccer')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 12 < now.day:
        allow_change = False
    elif 12 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_soccerSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-soccer/')

    else:
        form = womens_soccerSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_soccer(request):
    userselection = mens_soccerSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-soccer')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 13 < now.day:
        allow_change = False
    elif 13 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_soccerSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-soccer/')

    else:
        form = mens_soccerSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_womens_beach_volleyball(request):
    userselection = womens_beach_volleyballSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-beach-volleyball')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 16 < now.day:
        allow_change = False
    elif 16 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_beach_volleyballSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-beach-volleyball/')

    else:
        form = womens_beach_volleyballSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_waterpolo(request):
    userselection = mens_waterpoloSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-waterpolo')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 16 < now.day:
        allow_change = False
    elif 16 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_waterpoloSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-waterpolo/')

    else:
        form = mens_waterpoloSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_womens_bmx(request):
    userselection = womens_bmxSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='womens-bmx')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 19 < now.day:
        allow_change = False
    elif 19 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = womens_bmxSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/womens-bmx/')

    else:
        form = womens_bmxSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required
def selection_mens_bmx(request):
    userselection = mens_bmxSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-bmx')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 19 < now.day:
        allow_change = False
    elif 19 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_bmxSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-bmx/')

    else:
        form = mens_bmxSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})

@login_required    
def selection_mens_handball(request):
    userselection = mens_handballSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='mens-handball')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 17 < now.day:
        allow_change = False
    elif 17 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True 
        
    if request.method == "POST":
        form = mens_handballSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/mens-handball/')

    else:
        form = mens_handballSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})
    
@login_required    
def selection_show_jumping(request):
    userselection = show_jumpingSelection.objects.filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    sport = get_object_or_404(Sport, sport_slug='show-jumping')
    now = datetime.datetime.now()
    allow_change = True
    if 7 == now.month:
        allow_change = True
    elif 19 < now.day:
        allow_change = False
    elif 19 == now.day and 0 <= now.hour:
        allow_change = False
    elif 8 < now.month:
        allow_change = False
    else:
        allow_change = True    
    if request.method == "POST":
        form = show_jumpingSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.save()
            return redirect ('/sports/show-jumping/')

    else:
        form = show_jumpingSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'sport': sport, 'userselection': userselection, 'allow_change': allow_change})