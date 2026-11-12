from django.db import models

# Create your models here.


# ==== classe Table ====

class Place ( models.Model ):
	num_place : models.CharField( max_length = 20 )
	nbr_pers : models.IntegerField ()


# ==== classe Client ====

class Client ( models.Model ):
	place : models.ForeignKey ( Place , on_delete = models.PROTECT )
	nom_cli : models.CharField ( max_length = 100 )
	date_visite : models.DateField ()
	heur_arrive : models.DateTimeField ()
	heur_depart : models.DateTimeField ()
	contact : models.CharField ( max_length = 60 )

#	def __str__ ( self ):
#		return " Client table %s du %s de %s à %s heures " % ( self.table , self.date_visite , self.heur_arrive , self.heur_depart )


# ==== classe Produit ====

class Produit ( models.Model ):
	nom_produit : models.CharField ( max_length = 200 )
	prix_vente : models.IntegerField ()

#	def ___str__ ( self ):
#		return  " %s : %s Ar " % ( self.nom_produit , self.prix_vente  )


# ==== classe Commande ====

class Commande ( models.Model ):
	nom_cli : models.ManyToManyField ( Client )
	nom_produit : models.ManyToManyField ( Produit )
	qte_commande : models.IntegerField ()
