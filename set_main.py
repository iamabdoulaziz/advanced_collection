# Colllection : Set
"""
J'apprends en même temps que le set n'a pas de notion d'ordre par contre
 garantie de ne pas avoir de doublons dans la liste.

 // On peut énumérer également un set mais pas d'indexation !
 // On peut par contre retransformé le set en une list grâce à la fonction list.
 // Set se construis comme un dictionnaire mais avec les accolades (des clés sans valeurs, genre pas de : pour associer
    à une valeur !

"""

names = ["Mimich", "Adbramane", "Bahama", "Blueface", "Cute Boy", "Cute Boy"]
print(names)
set_names = set(names)
names_without_doublons = list(set(names))
names_set = {"Mimich", "Mimich", "Adbramane", "Bahama", "Blueface", "Cute Boy", "Cute Boy"}
print(set_names)
print(set_names)
print(names_without_doublons)
