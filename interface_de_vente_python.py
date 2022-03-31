#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:24:36 2022

@author: jeremie
"""
#Diagramme de classe Page 1


class Article:
    def __init__(self,idArticle,photo,titre,description,prix,catégorie,couleur,taille,quantité):
        self.idArticle = idArticle
        def getidArticle(self):
            return self.idArticle
        
        self.photo = photo
        
        def getphoto(self):
            return self.photo
        
        self.titre = titre
        def gettitre(self):
            return self.titre
        
        self.description = description
        def getdescription(self):
            return self.description
        
        self.prix = prix
        def getprix(self):
            return self.prix
        
        self.catégorie = catégorie
        def getcatégorie(self):
            return self.catégorie
        
        self.couleur = couleur
        def getcouleur(self):
            return self.couleur
        
        self.taille = taille
        def gettaille(self):
            return self.taille
        
        self.quantité = quantité
        def getquantité(self):
            return self.quatité
        
        
class Commande():
    def __init__(self,idCommande,prixTotal,état,date,heure):
        self.idCommande = idCommande
        def getidCommande(self):
            return self.idCommande
        
        
        self.prixTotal = prixTotal
        def getprixTotal(self):
            return self.prixTotal
        
        self.état = état
        def getétat(self):
            return self.état
        
        self.date = date
        def getdate(self):
            return self.date
        
        self.heure = heure
        def getheure(self):
            return self.heure
        
        
    
        
class Utilisateur():
    def __init__(self,identifiantUtilisateur,motDePasse,nom,Prénom):
        self.identifiantUtilisateur = identifiantUtilisateur
        def getidentifiantUtilisateur(self):
            return self.identifiantUtilisateur
        
        
        self.motDePasse = motDePasse
        def getmotDePasse(self):
            return self.motDePasse
        
        self.nom = nom
        def getnom(self):
            return self.nom
        
        self.Prénom = Prénom
        def getPrénom(self):
            return self.Prénom
        
class Client(Utilisateur):
    def __init__(self,dateDeNaissance,adresse,style,age,genre,mensualité):
        self.dateDeNaissance = dateDeNaissance
        def getdateDeNaissance(self):
            return self.dateDeNaissance
        
        
        self.adresse = adresse
        def getadresse(self):
            return self.adresse
        
        self.style = style
        def getstyle(self):
            return self.style
        
        self.age = age
        def getage(self):
            return self.age

             
        self.genre = genre
        def getgenre(self):
            return self.genre
        
        self.mensualité = mensualité
        def getmensualité(self):
            return self.mensualité

#        class Employé(Utilisateur):
#      def __init__()
 
        #Diagramme de séquence

def Interface_vente_en_ligne(c):
    client = c.object('Client')
    interface = c.object('Interface')
    base_de_donnees_compte_utilisateur = c.object('Base de donnée compte utilisateur')
    base_de_donnees_article = c.object('Base de données article')
    base_de_donnees_commandes = c.object('Base de données commandes')
    employe_entrepot = c.object('Employé entrepôt')

    with client:
        with interface.Creation_compte_client():
            client.ret('Creation Reussi')
            client.ret('Renvoie  formulaire')
            interface.ret('Remplie formulaire')
            client.ret('Renvoie de recommandation')
            with interface.Ajouter_article_au_panier().ret('Afficher panier'):
                interface.ret('Valide panier')
                client.ret('Page de paiement')
                interface.ret('Procède au paiment')
                clien.ret('Confirme la commande')
                with interface.Authentification():
                    base_de_donnees_compte_utilisateur.Requete_compte_utilisateur().ret('Valide authentification')
                    with employe_entrepot.Authentification_reussie():
                        with interface.Afficher_article():
                            base_de_donnees_article.Requete_article().ret('Renvoie liste articles')
                            employe_entrepot.ret('Liste arcticle')
                            with interface