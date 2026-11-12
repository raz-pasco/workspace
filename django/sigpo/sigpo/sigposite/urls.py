from sigposite.views import *
from django.urls import path
from . import views

urlpatterns = [
	# ex: /polls/
#	path('', views.index, name='index'),
	# ex: /caisse/5/
	path('', CompteList.as_view(), name = 'index'),
	path('nonlivre/', CompteList.as_view(livre = True), name = 'nonlivre'),
	path('nouveau/', CompteList.as_view(compte = True), name = 'nouveau'),
	path('ticket/<int:table_id>', TicketPdf.as_view(), name = 'ticket'),
	path('table/<int:table_id>', TablePdf.as_view(), name = 'table'),
	path('PDFaddition/<int:table_id>', PdfView.as_view(), name = 'PDFaddition'),
	path('ajouter/<int:table_id>', ListArticle.as_view(), name = 'ajouter'),
	path('confirmer/<int:table_id>', ListArticle.as_view(add = True), name = 'confirmer'),
#	path('inserer/<int:table_id>', ListArticle.as_view(add = True), name = 'inserer'),
	path('vente/', VenteList.as_view(), name = 'vente'),
	path('control/', FormControl.as_view(), name = 'control'),
	path('ral/', RalList.as_view(), name = 'ral'),
	path('livret/<int:table_id>', CommandeList.as_view(livre = True), name = 'livrer'),
	path('payer/<int:table_id>', CommandeList.as_view(paye = True), name = 'payer'),
	path('partiel/<int:table_id>', CommandeList.as_view(part = True), name = 'partiel'),
	path('commande/<int:table_id>', CommandeList.as_view(), name = 'commandes'),
#	path('commandes/<int:table_id>', views.commandes, name='commandes'),
	path('addcommande/', GetCommande.as_view()),
	path('form/<int:table_id>', ListBtCommande.as_view(), name = 'form'),
	# ex: /sigposite/5/cuisine/
	path('<int:commande_id>/cuisine/', views.cuisine, name='cuisine'),
	# ex: /sigposite/5/livraison/
	path('<int:commande_id>/livraison/', views.livraison, name='livraison'),
]
