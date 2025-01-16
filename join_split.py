# LIDTES AND TUPLES
#Join and Split

names = ["Safia", "Cute boy", "La Brute", "Pap", "Arthur", "Zeni"]


join_names = ", ".join(names)
print(names)
print(join_names)


a = "Mimich, Abdramane, Bahama"
a_split = a.split(", ")

print(a)
print(a_split)

reconstitute_names = join_names.split(", ")

print(reconstitute_names)