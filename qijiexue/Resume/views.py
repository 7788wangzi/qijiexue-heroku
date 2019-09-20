from django.shortcuts import render
from django.http import HttpRequest
from .models import Contact

# Create your views here.

def index(request):
    """Renders the home page."""
    if request.method == 'POST':
        name_r = request.POST.get('name')
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(name=name_r, email=email_r, subject = subject_r, message=message_r)
        c.save()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Resume/index.html',
        {
            'title':'Home - Qijie Resume'
        }
    )

def gallery(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Resume/img-gallery.html',
        {
            'title': 'Picture gallery'
        }
    )

def animation(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Resume/animation.html',
        {
            'title':'Video Sample'
        }
    )

def projects(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Resume/projects.html',
        {
            'title':'Latest Projects'
        }
    )