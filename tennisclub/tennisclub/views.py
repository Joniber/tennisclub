from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import *
from .forms import *

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

    termine = Termine.objects.all().order_by('date')

    termineForm = TermineForm()

    return render(request, 'termine.html', {'termine':termine, 'termineForm': termineForm})


def createtermin_view(request):

    termineForm = TermineForm(data=request.POST)
    if termineForm.is_valid() and request.user.is_superuser:
        instance = termineForm.save(commit=False)
        instance.autor = request.user
        instance.save()
    return redirect('termine')

def terminedit_view(request, uuid):
    termin = Termine.objects.get(uuid=uuid)
    if request.method=='POST' and request.user.is_superuser:
        termin.bezeichnung = request.POST.get('editbezeichnung')
        if request.POST.get('editdate') != "":
            termin.date = request.POST.get('editdate')
        if request.POST.get('edittime') != "":
            termin.time = request.POST.get('edittime')
        termin.location = request.POST.get('editlocation')
        termin.save()
        
    return redirect('termine')

def termindelete_view(request, uuid ):
    termin = Termine.objects.get(uuid=uuid)
    
    if request.method=='POST' and request.user.is_superuser:
        termin.delete()
    return redirect('termine')

def schule_view(request):
    return render(request, 'schule.html')
def anfahrt_view(request):
    return render(request, 'anfahrt.html')
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


def login_view(request):
    
    if request.method == 'POST':
        loginform = AuthenticationForm(data=request.POST)
        if loginform.is_valid():
            
            user = loginform.get_user()
            
            login(request, user)
                       
            return redirect('/')
            
    else:
        loginform = AuthenticationForm()
    return render(request, 'login.html', {'loginform':loginform})


def blog_view(request):

    blogForm = BlogForm()
    blogPosts = BlogPost.objects.all().order_by('-creation')
    print(blogPosts)

    return render(request, 'blog.html', {'blogForm': blogForm, 'blogPosts': blogPosts})


def createblogPost_view(request):

    blogForm = BlogForm(request.POST, request.FILES)
    print(blogForm)
    if blogForm.is_valid() and request.user.is_superuser:
        print('hello?')
        instance = blogForm.save(commit=False)
        instance.autor = request.user
        instance.save()
    return redirect('blog')

def blogPostedit_view(request, uuid):
    blogPost = BlogPost.objects.get(uuid=uuid)
    if request.method=='POST' and request.user.is_superuser:
        blogPost.titel = request.POST.get('edittitel')
        blogPost.inhalt = request.POST.get('editinhalt')

        if request.POST.get('editdate') != "":
            blogPost.date = request.POST.get('editdate')
        
        if request.FILES.get('editbild') != "":
            print(request.FILES.get('editbild'))
            blogPost.bild = request.FILES.get('editbild')
        print('Wenn du das hier alleine siehst hast du einen Fehler!')
        blogPost.standort = request.POST.get('editstandort')
        blogPost.save()
        
    return redirect('blog')

def blogPostdelete_view(request, uuid ):
    blogPost = BlogPost.objects.get(uuid=uuid)
    
    if request.method=='POST' and request.user.is_superuser and blogPost.autor == request.user:
        blogPost.delete()
    return redirect('blog')