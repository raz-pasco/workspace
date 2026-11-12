from django.contrib import admin

# Register your models here.
from .models import Place , Client , Produit , Commande  

admin.site.register( Place )
admin.site.register( Client )
admin.site.register( Produit )
admin.site.register( Commande  )
