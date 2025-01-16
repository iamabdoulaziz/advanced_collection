# LISTES AND TUPLES
# Swapping two elements

names = ["Safia", "Cute boy", "La Brute", "Pap", "Arthur", "Zeni"]

"""
t = names[0]
names[0] = names[1]
names[1] = t
"""
# Atomic maner
names[0], names[1] = names[1], names[0]

print(names)
