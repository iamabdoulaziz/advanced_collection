# Lists and Tuples
# Comprehensions of lists

names = ["Arthur", "Saphia", "Cute", "El Brute", "Pap", "Zeni", "AZERTY-QWERTY"]

"""
names_len = []
for name in names:
    names_len.append(len(name))
"""

#print(names_len)

#names_len = [len(name) for name in names]
names_len = [len(name) for name in names if len(name) < 10]
print(names_len)

name_with_e = [name for name in names if "e" in name]
print(name_with_e)

a = [i for i in range(10) if (i//2)*2 == i]
print(a)

b = [(i, True if (i//2)*2 == i else False) for i in range(11)]
print(b)