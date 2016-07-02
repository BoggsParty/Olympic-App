from django.shortcuts import get_object_or_404, render, redirect
from .models import Sport 
from UserSelections.models import eventingSelection, womens_all_around_gymnasticsSelection, mens_all_around_gymnasticsSelection, womens_track_4x100_relaySelection, mens_track_4x100_relaySelection, womens_decathalonSelection, mens_decathalonSelection, womens_swimming_4x100_medley_relaySelection, mens_swimming_4x100_medley_relaySelection, womens_swimming_200m_backstrokeSelection, mens_swimming_1500m_freestyleSelection, mens_golfSelection, womens_basketballSelection, womens_soccerSelection, mens_soccerSelection, womens_beach_volleyballSelection, mens_waterpoloSelection, womens_bmxSelection, mens_bmxSelection, mens_handballSelection, show_jumpingSelection
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def menu(request):
    sport = Sport.objects.order_by('order')
    return render(request, 'CountryInfo/sportmenu.html', {'sport': sport})
 
@login_required 
def eventing_detail(request):
    sport = get_object_or_404(Sport, sport_slug='eventing')
    userselection = eventingSelection.objects.filter(Q(sport_name='eventing') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})
    
@login_required 
def womens_all_around_gymnastics_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-all-around-gymnastics')
    userselection = womens_all_around_gymnasticsSelection.objects.filter(Q(sport_name='womens-all-around-gymnastics') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required 
def mens_all_around_gymnastics_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-all-around-gymnastics')
    userselection = mens_all_around_gymnasticsSelection.objects.filter(Q(sport_name='mens-all-around-gymnastics') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})
    
@login_required
def womens_track_4x100_relay_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-track-4x100-relay')
    userselection = womens_track_4x100_relaySelection.objects.filter(Q(sport_name='womens-track-4x100-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_track_4x100_relay_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-track-4x100-relay')
    userselection = mens_track_4x100_relaySelection.objects.filter(Q(sport_name='mens-track-4x100-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})
    
@login_required
def womens_decathalon_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-decathalon')
    userselection = womens_decathalonSelection.objects.filter(Q(sport_name='womens-decathalon') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_decathalon_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-decathalon')
    userselection = mens_decathalonSelection.objects.filter(Q(sport_name='mens-decathalon') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})
    
@login_required
def womens_swimming_4x100_medley_relay_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-swimming-4x100-medley-relay')
    userselection = womens_swimming_4x100_medley_relaySelection.objects.filter(Q(sport_name='womens-swimming-4x100-medley-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_swimming_4x100_medley_relay_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-swimming-4x100-medley-relay')
    userselection = mens_swimming_4x100_medley_relaySelection.objects.filter(Q(sport_name='mens-swimming-4x100-medley-relay') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def womens_swimming_200m_backstroke_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-swimming-200m-backstroke')
    userselection = womens_swimming_200m_backstrokeSelection.objects.filter(Q(sport_name='womens-swimming-200m-backstroke') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_swimming_1500m_freestyle_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-swimming-1500m-freestyle')
    userselection = mens_swimming_1500m_freestyleSelection.objects.filter(Q(sport_name='mens-swimming-1500m-freestyle') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_golf_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-golf')
    userselection = mens_golfSelection.objects.filter(Q(sport_name='mens-golf') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def womens_basketball_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-basketball')
    userselection = womens_basketballSelection.objects.filter(Q(sport_name='womens-basketball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def womens_soccer_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-soccer')
    userselection = womens_soccerSelection.objects.filter(Q(sport_name='womens-soccer') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_soccer_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-soccer')
    userselection = mens_soccerSelection.objects.filter(Q(sport_name='mens-soccer') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def womens_beach_volleyball_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-beach-volleyball')
    userselection = womens_beach_volleyballSelection.objects.filter(Q(sport_name='womens-beach-volleyball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_waterpolo_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-waterpolo')
    userselection = mens_waterpoloSelection.objects.filter(Q(sport_name='mens-waterpolo') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def womens_bmx_detail(request):
    sport = get_object_or_404(Sport, sport_slug='womens-bmx')
    userselection = womens_bmxSelection.objects.filter(Q(sport_name='womens-bmx') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})

@login_required
def mens_bmx_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-bmx')
    userselection = mens_bmxSelection.objects.filter(Q(sport_name='mens-bmx') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})
    
@login_required
def mens_handball_detail(request):
    sport = get_object_or_404(Sport, sport_slug='mens-handball')
    userselection = mens_handballSelection.objects.filter(Q(sport_name='mens-handball') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})
    
@login_required
def show_jumping_detail(request):
    sport = get_object_or_404(Sport, sport_slug='show-jumping')
    userselection = show_jumpingSelection.objects.filter(Q(sport_name='show-jumping') | Q(sport_name='none')).filter(Q(user=request.user) | Q(user__isnull=True)).latest('date_created')
    return render(request, 'CountryInfo/sportdetail.html', {'userselection':userselection, 'sport':sport,})