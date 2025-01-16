
name = ["Jean", "Sophie", "Martin", "Cute boy"]
#name.append("Cute girl")
#intermediare_list = ["La brute", "Arthur"]
#name.extend(intermediare_list)
#name.insert(0, "Pap")
#name.insert(1, "Zeni")
# Slices precision
name_slices = name[:]

name.sort(reverse= True) #sort by alphabetique letter starting bye Z cause reverse is true,bye default it's A
sorted_name = sorted(name)

name.sort(key=lambda x : len(x), reverse= True)

print(name)
print(sorted_name)
