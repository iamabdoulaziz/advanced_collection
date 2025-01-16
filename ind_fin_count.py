# LISTES AND TUPLES
# Index, Find and Count

names = ["Safia", "Cute boy", "La Brute", "Pap", "Arthur", "Zeni", "Safia"]

print(names.index('Cute boy'))

search_element = "Safia"

"""
if search_element in names:
    print(names.index(search_element))
else:
    print("Element does'nt exist in the collection !")
"""

occurences_nb = names.count(search_element)
print("Occurence number = ", occurences_nb)
if occurences_nb > 0:
    index_occurence = 0
    for i in range(occurences_nb):
        index_occurence = names.index(search_element, index_occurence)
        print(search_element, "find at", index_occurence)
        index_occurence += 1
else:
    print("Element does'nt exist in the collection !")

#Find is not applicable to list
a = "Jean-Martin-Toto"
i = a.find("martin")
print(i)
