"""tennisclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name="index"),
    path('kontakt/', views.kontakt_view, name="kontakt"),
    path('verein/', views.verein_view, name="verein"),
    path('verein/beitrag', views.beitrag_view, name="beitrag"),
    path('verein/team', views.team_view, name="team"),
    path('verein/heim', views.heim_view, name="heim"),


    path('verein/termine', views.termine_view, name="termine"),
    path('createtermin', views.createtermin_view, name='createtermin'),
    path('<str:uuid>/terminbearbeiten', views.terminedit_view, name='terminedit'),
    path('<str:uuid>/termindelete', views.termindelete_view, name='termindelete'),


    path('blog/', views.blog_view, name='blog'),
    path('createblogPost', views.createblogPost_view, name='createblogPost'),
    path('<str:uuid>/blogPostbearbeiten', views.blogPostedit_view, name='blogPostedit'),
    path('<str:uuid>/blogPostdelete', views.blogPostdelete_view, name='blogPostdelete'),


    path('tennis/schule', views.schule_view, name="schule"),
    path('tennis/courts', views.courts_view, name="courts"),
    path('tennis/regeln', views.regeln_view, name="regeln"),
    path('sitemap',views.sitemap_view, name='sitemap'),
    path('impressum',views.impressum_view, name='impressum'),
    path('login/', views.login_view, name="login"),




    
]
