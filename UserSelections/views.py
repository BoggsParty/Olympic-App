from django.shortcuts import get_object_or_404, render, redirect
from .models import UserSelection
from CountryInfo.models import Sport
from .forms import UserSelectionForm
from django.contrib.auth.decorators import login_required

@login_required
def selection(request, sport_slug):
    lookup_field = 'sport_slug'
    active_sport = get_object_or_404(Sport, sport_slug=sport_slug)
    #return render(request, 'UserSelections/submit.html', {'active_sport':active_sport})
    
    if request.method == "POST":
        form = UserSelectionForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            selection.user = request.user
            selection.sport_name = active_sport.sport_slug
            selection.save()
            return redirect("/sports/")
    else:
        form = UserSelectionForm()
    return render(request, 'UserSelections/submit.html', {'form': form, 'active_sport':active_sport})   
    
