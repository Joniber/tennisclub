from django.contrib import admin
from .models import BlogPost, Galerie, Kommentar, Termine

admin.site.register(BlogPost)
admin.site.register(Termine)
admin.site.register(Kommentar)
admin.site.register(Galerie)