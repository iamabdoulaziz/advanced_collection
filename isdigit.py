"""
def _isdigit(chaine):
     for c in chaine:
         if c.isdigit():
             return True
     return False

name = input("Quel est ton nom ? : ")
if name == "":
    print("Le nom est vide")
elif _isdigit(name):
    print("Ce nom est invalide, il ne doit pas contenir de chiffres")
else:
    print(f"Bonjour {name}")
"""
name = "name123"
digit_name = any([c.isdigit() for c in name])
print(digit_name)
