import uu
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from datetime import date, timedelta
from django.contrib.auth import login, logout
from .models import *
from .forms import *
from .filters import *

def index_view(request):
    startdate = date.today()
    enddate = startdate - timedelta(days=14)
    blogPosts = BlogPost.objects.all().filter(date__range=[enddate, startdate]).order_by('-date')[:3]
    termineenddate = startdate + timedelta(days=14)
    nextTermin = Termine.objects.all().filter(date__range=[startdate, termineenddate]).order_by('date')[:1].first()
    print(termineenddate)
    print(nextTermin)
    return render(request, 'index.html', {'blogPosts': blogPosts, 'termin': nextTermin})

def kontakt_view(request):
    return render(request, 'kontakt.html')

def beitrag_view(request):
    return render(request, 'beitrag.html')

def team_view(request):
    return render(request, 'team.html')
def rückblick_view(request):
    return render(request, 'heim.html')

def termine_view(request):
    
    termine = Termine.objects.all().order_by('date')
    myFilter = TerminFilter(request.GET, queryset=termine) 
    termine = myFilter.qs

    termineForm = TermineForm()

    return render(request, 'termine.html', {'termine':termine, 'termineForm': termineForm, 'myFilter': myFilter})


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
def courts_teppichboden_preise_view(request):
    return render(request, 'courts_teppichboden_preise_view.html')
def courts_Traglufthalle_preise_preise_view(request):
    return render(request, 'courts_Traglufthalle_preise_preise_view.html')
def courts_teppichbodenhalle(request):
    return render(request, 'teppichbodenhalle.html')
def courts_traglufthalle(request):
    return render(request, 'traglufthalle.html')



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
    blogPosts = BlogPost.objects.all().order_by('-date')
    myFilter = BlogFilter(request.GET, queryset=blogPosts) 
    blogPosts = myFilter.qs

    return render(request, 'blog.html', {'blogForm': blogForm, 'blogPosts': blogPosts, 'myFilter': myFilter, })


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
        print(request.FILES.get('editbild'))
        if request.FILES.get('editbild') != None:
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

def blogPostDetail_view(request, uuid):
    blogPost = BlogPost.objects.get(uuid=uuid)
    kommentare = Kommentar.objects.filter(blogPost_reffering__uuid = uuid)
    kommentarForm = KommentarForm
    
    return render(request, 'blogPostDetail.html', {'blogPost': blogPost, 'kommentarForm': kommentarForm, 'kommentare': kommentare})

def galerie_view(request):
    galerie = Galerie.objects.all()
    galerieForm = GalerieForm
    return render(request, 'galerie.html', {'galerie': galerie, 'galerieForm': galerieForm})

def addgaleriebild_view(request):
    if request.method == 'POST':
        galerieForm = GalerieForm(request.POST, request.FILES)
        if galerieForm.is_valid() and request.user.is_superuser:
            instance = galerieForm.save(commit=False)
            
            instance.autor = request.user
            instance.save()
    return redirect('galerie')

def galeriebildbearbeiten_view(request, uuid):
    bild = Galerie.objects.get(uuid=uuid)
    if request.method=='POST' and request.user.is_superuser:
        bild.beschreibung = request.POST.get('editbeschreibung')
 
        if request.POST.get('editdate') != "":
            bild.date = request.POST.get('editdate')
        if request.FILES.get('editbild') != None:
            bild.bild = request.FILES.get('editbild')
        bild.standort = request.POST.get('editstandort')
        bild.save()
        
    return redirect('galerie')

def galeriebilddelete_view(request, uuid ):
    bild = Galerie.objects.get(uuid=uuid)
    
    if request.method=='POST' and request.user.is_superuser:
        bild.delete()
    return redirect('galerie')


def logout_view(request):


    logout(request)
    return redirect('index')

def kommentar_erstellen_view(request, uuid):
    if request.method == 'POST':
        kommentarForm = KommentarForm(request.POST)
        print(kommentarForm)
        if kommentarForm.is_valid():
            instance = kommentarForm.save(commit=False)
            instance.blogPost_reffering = BlogPost.objects.get(uuid=uuid)
            print(instance.blogPost_reffering)
            instance.save()
            if 'error_message' in request.session:
                del request.session['error_message']
        else:
            request.session['error_message'] = 'Bitte trage eine valide Email ein'
            return redirect('/blog/' + uuid)
    return redirect('/blog/'+ uuid)

def kommentar_delete_view(request, uuid):
    if request.method == 'POST' and request.user.is_superuser:
        kommentar = Kommentar.objects.get(uuid=uuid)

        url = kommentar.blogPost_reffering.uuid
       
        kommentar.delete()
    return redirect('/blog/'+ str(url))

def stoperror_view(request):
    if 'error_message' in request.session:
                del request.session['error_message']

    url = request.META.get('HTTP_REFERER')
    return redirect(url)

    