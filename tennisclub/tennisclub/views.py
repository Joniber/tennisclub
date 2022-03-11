from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def index_view(request):
    return render(request, 'index.html')

def kontakt_view(request):
    return render(request, 'kontakt.html')

def beitrag_view(request):
    return render(request, 'beitrag.html')

def team_view(request):
    return render(request, 'team.html')
def heim_view(request):
    return render(request, 'heim.html')

def termine_view(request):
    return render(request, 'termine.html')
def schule_view(request):
    return render(request, 'schule.html')
def courts_view(request):
    return render(request, 'courts.html')
def regeln_view(request):
    return render(request, 'regeln.html')

def sitemap_view(request):
    return render(request, 'sitemap.html')
def impressum_view(request):
    return render(request, 'impressum.html')
def verein_view(request):
    return render(request, 'verein.html')
