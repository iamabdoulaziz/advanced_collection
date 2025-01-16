# Coolections : LISTS AND TUPLES
# EXERCISE "total number of char... in the collections"


names = ["Cute boy", "El Brute", "Pap", "Dumbo", "Zeni", "Jinx"]

"""
My try
len_list = []
for e in names:
    e_len = len(e)
    len_list.append(e_len)

print(sum(len_list))"""
s = 0
"""
#1 - for / len
for name in names:
    s += len(name)
print(f"Nombre total de caractères dans la liste : {s}|")"""

"""
# 2 - List completion + sum
list_sum = [(len(name)) for name in names ]
print("Nombre total de caractères dans la liste :", sum(list_sum))"""

#  3 - Join and len
for name in names:
    sum_element =','.join(name) #Eurrk not good don't do that
    # Do that ...
print("Nombre total de caractères dans la liste :", len("".join(names)))

