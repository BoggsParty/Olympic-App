from django.shortcuts import get_object_or_404, render, redirect
from .models import Sport 
from UserSelections.models import UserSelection
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def menu(request):
    sport = Sport.objects.all()
    return render(request, 'CountryInfo/sportmenu.html', {'sport': sport})
 
@login_required 
def detail(request, sport_slug):
    lookup_field = 'sport_slug'
    sport = get_object_or_404(Sport, sport_slug=sport_slug)
    userselection = UserSelection.objects.filter(Q(sport_name=sport_slug) | Q(sport_name='none')).filter(user=request.user).order_by('-id')[0]
    return render(request, 'CountryInfo/sportdetail.html', {'sport':sport, 'userselection':userselection})
