from django.contrib import admin
from .models import Compte , Client , Produit , Commande

# Register your models here.

admin.site.register( Compte )
admin.site.register( Client )
admin.site.register( Produit )
admin.site.register( Commande )
