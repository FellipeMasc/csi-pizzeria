from pizza import *


# Exemplo:
#1. Pizza de frango catupiry
pizza_frango_catupiry = BasePizza()
pizza_frango_catupiry = CatupiryCheese(pizza_frango_catupiry)
pizza_frango_catupiry = Chicken(pizza_frango_catupiry)
pizza_frango_catupiry = Olives(pizza_frango_catupiry)

print("Pizza de frango catupiry:")
print(f"Ingredientes: {pizza_frango_catupiry.get_description()}")
print(f"Custo: {pizza_frango_catupiry.get_cost()}")


#2. Pizza de calabresa
pizza_calabresa = BasePizza()
pizza_calabresa = MozzarellaCheese(pizza_calabresa)
pizza_calabresa = Onions(pizza_calabresa)
pizza_calabresa = Pepperoni(pizza_calabresa)
pizza_calabresa = Olives(pizza_calabresa)

print("Pizza de calabresa:")
print(f"Ingredientes: {pizza_calabresa.get_description()}")
print(f"Custo: {pizza_calabresa.get_cost()}")