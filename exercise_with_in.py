

names = ["Jean", "Sophie", "Martin", "Cute boy", "Zoe", "Martin"]
#lower_names = [l_name.lower() for l_name in names]
#print(lower_names)
"""
if "Jean" in names:
    print ("Jean est là")
else:
    print("Nan il n'est pas là")
"""

"""
def element_in_list(e, l):
    return e.lower() in l

if element_in_list("Jean", lower_names):
    print('Il est là !')
else:
    print("Non il n'est là !")
"""
def element_in_list(e, l):
    for el in l:
        if e.lower() == el.lower():
            return True
    return False

if element_in_list("Jean", names):
    print("Trouvé !")
else:
    print("Nan pas trouvé !")
