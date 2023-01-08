"""
Dans le fichier "boucle_automatisation.py, vous trouverez : les fonctions pour ajouter un nom, 
un prénom, la date d'arrivée du nouvel employé, son poste ainsi que le nom de la personne qui l'ajoute.
Le tout est ensuite implémenté dans un dataframe pandas puis transformé en fichier.csv.
"""

import pandas as pd
import numpy as np
import inquirer

from liste_metier import metiers
from datetime import datetime

#Convention : Nom, Prénom, Date embauche, Poste



#fonction case du nom 
def surname():
    print("Consigne : le nom ne doit pas contenir de chiffre et comporter moins de 15 caractères")
    a = input("Entrez le nom du nouvel employé : ")
    return a


def name():
    print("Consigne : le nom ne doit pas contenir de chiffre et comporter moins de 15 caractères")
    b = input("Entrez le prénom du nouvel employé : ")
    return b.title()


def time():
    """
    Cette fonction permet de d'indiquer la date au format jj/MM/AAAA

    """

    j = input("""Entrez le jour du mois d'arrivée : 
    il doit être composé de 2 chiffres -ex : pour le premier du mois, écrivez 01- :""")
    m = input ("""Etrez le mois d'arrivée : 
    il doit être composé de 2 chiffres -ex : pour le mois de mars, écrivez 03- :""")
    y = input ("""entrée l'année d'arrivée : 
    il doit être composé de 4 chiffres""")
    date = print(f"{j}/ {m} /{y}")
                 
    return date


def position(choix_metier):
    """
    Cette fonction définit une fonction appelée position qui prend en paramètre choix_metier et renvoie la position choisie 
    par l'utilisateur. Il utilise la bibliothèque inquirer pour demander à l'utilisateur de sélectionner une position dans 
    la liste de choix passée en paramètre de la fonction List. La position sélectionnée par l'utilisateur est renvoyée 
    sous forme de chaîne de caractères grâce à la clé position du dictionnaire answers.
    """

    questions = [inquirer.List('position', message = "Quel position souhaitez-vous ?",
                                choices = choix_metier,),]
    answers = inquirer.prompt(questions)

    return answers['position']



def prescripteur():
    e = input("Entrez votre nom : ")
    return e


def ajout_auto(data):
    """
    Ce code définit une fonction appelée ajout_auto qui prend en paramètre data et renvoie un résultat res. Elle ajoute
    une nouvelle ligne au dataframe data à l'index len(data), qui correspond à la dernière ligne du dataframe. La nouvelle
    ligne est une liste contenant les valeurs nom, prenom, date, poste, prescri et la date et l'heure courantes.

    Pour utiliser cette fonction, vous pouvez l'appeler et lui passer un dataframe en tant que paramètre data. La fonction 
    ajoutera alors une nouvelle ligne au dataframe avec les valeurs spécifiées et renverra le résultat.
    """

    res = data.loc[len(data)]=[nom, prenom, date, poste, prescri, datetime.now()]
    
    return res

# if __name__ == "__main__":
    df = pd.read_csv(r'liste_employes.csv', index_col=0)
    df['Prescripteur'] = np.nan
    df['Date_ajout'] = np.nan

    choix_metier = metiers()

    nom = surname().upper()
    prenom = name()
    date = time()
    poste = position(choix_metier)
    print(poste)
    prescri = prescripteur()
    print(df)
    ajout_auto(df)
    print(df)

    df.to_csv('liste_employes.csv', sep=",")




