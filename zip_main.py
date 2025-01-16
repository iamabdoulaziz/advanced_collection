
# La function zip sert à regrouper plusieurs listes sous la forme d'un tuples

pizzas_names = ("4 fromages", "Calzone", "Hawaï")
pizzas_prices = (4000, 3000, 2500)

pizzas_names_and_prices = list(zip(pizzas_names, pizzas_prices))

for name, price in pizzas_names_and_prices:
    print(f"{name} - {price} FCFA")

unzipped = list(zip(*pizzas_names_and_prices))
print(unzipped)
unz_pizza_name, unz_pizza_price = list(zip(*pizzas_names_and_prices))
print(unz_pizza_name)
print(unz_pizza_price)
