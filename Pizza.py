from abc import ABC, abstractmethod

class PizzaComponent(ABC):
    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

class BasePizza(PizzaComponent):
    def __init__(self):
        self.description = "Massa da pizza"

    def get_description(self):
        return self.description

    def get_cost(self):
        return 10.00

class PizzaDecorator(PizzaComponent):
    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description()

    def get_cost(self):
        return self.pizza.get_cost()

class MozzarellaCheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Queijo mussarela"

    def get_cost(self):
        return self.pizza.get_cost() + 2.00
    
class CatupiryCheese(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Queijo catupiry"

    def get_cost(self):
        return self.pizza.get_cost() + 3.00

class Pepperoni(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Calabresa"

    def get_cost(self):
        return self.pizza.get_cost() + 2.00

class Olives(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Azeitona"

    def get_cost(self):
        return self.pizza.get_cost() + 0.60

class Mushrooms(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Cogumelo"

    def get_cost(self):
        return self.pizza.get_cost() + 1.00

class Onions(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Cebolas"

    def get_cost(self):
        return self.pizza.get_cost() + 0.90

class Bacon(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Bacon"

    def get_cost(self):
        return self.pizza.get_cost() + 3.00
    
class Shrimp(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Camarão"

    def get_cost(self):
        return self.pizza.get_cost() + 10.00
    
class Eggs(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Ovos"

    def get_cost(self):
        return self.pizza.get_cost() + 2.00
    
class Chicken(PizzaDecorator):
    def __init__(self, pizza):
        super().__init__(pizza)

    def get_description(self):
        return self.pizza.get_description() + ", Frango"

    def get_cost(self):
        return self.pizza.get_cost() + 5.00

