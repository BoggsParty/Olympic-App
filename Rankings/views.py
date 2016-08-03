from django.shortcuts import get_object_or_404, render, redirect
from .models import Comments_On, Comments
from .forms import CommentsForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

@login_required
def all_comments(request):
    comments = Comments.objects.all().order_by('-date_created')
    show_comments = True
    comment_boolean = Comments_On.objects.latest('pk')
    if comment_boolean.comments_on:
        show_comments = True
    else:
        show_comments = False 
    return render(request, 'Rankings/all_comments.html', {'comments': comments, 'show_comments':show_comments})
            
