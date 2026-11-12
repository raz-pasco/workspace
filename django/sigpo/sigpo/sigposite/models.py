from django.forms import ModelForm
from datetime import datetime
from django.db import models

# Create your models here.


# ==== classe Table ====

class Compte (models.Model):
	numero = models.CharField ( max_length = 20 , default = '' )
	personne = models.IntegerField ( default = 1)

	def __str__( self ):
		return ' %s ' % ( self.numero )

# ==== classe Client ====

class Client ( models.Model ):
	table = models.ForeignKey ( Compte , on_delete = models.PROTECT , default = '01' )
	nom = models.CharField ( max_length = 100 , blank = True )
	date_visite = models.DateField ( default = datetime.now , blank = True )
	heur_arrive = models.DateTimeField ( default = datetime.now , blank = True )
	heur_depart = models.DateTimeField ( default = datetime.now , blank = True )
	contact = models.CharField ( max_length = 60 , default = '' )

	def __str__ ( self ):
		return ' %s du %s de %s à %s heures ' % ( self.table , self.date_visite , self.heur_arrive , self.heur_depart )



# ==== classe Produit ====

class Produit ( models.Model ):
	designation = models.CharField ( max_length = 200 , default = '' )
	prix_vente = models.IntegerField ( default = 0 )

	def __str__ ( self ):
		return ' %s %s' % ( self.designation , self.prix_vente )


# ==== classe Commande ====

class Commande ( models.Model ):
	table = models.ForeignKey ( Compte , related_name = "table" , on_delete = models.PROTECT )
	date_cmd = models.DateField ( default = datetime.now , blank = True )
	heur_cmd = models.DateTimeField ( default = datetime.now , blank = True )
	designation = models.ForeignKey ( Produit , on_delete = models.PROTECT , default = "designation" )
	quantite = models.IntegerField ()
	livre = models.BooleanField ( default = False )
	paye = models.BooleanField ( default = False )

	def __str__( self ):
		return '%s %s %s %s ' % ( self.table , self.heur_cmd , self.quantite , self.designation )

# ==== form Commande ====
class CommandeForm(ModelForm):
	class Meta:
		model = Commande
		fields = ['table', 'designation', 'quantite']
