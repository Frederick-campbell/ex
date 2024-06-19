class PizzaComponent:
    def getDescription(self):
        return self.__class__.__name__
    def getCost(self):
        return self.__class__.cost
    
class Pizza(PizzaComponent):
    # all pizzas come with dough, tomato sauce and cheese
    cost = 5.0

class Decorator(PizzaComponent):
    def __init__(self, pizza_component):
        self.component = pizza_component

    def getCost(self): 
        return self.component.getCost() + PizzaComponent.getCost(self)
    
    def getDescription(self):
        return PizzaComponent.getDescription(self) + ' ' + self.component.getDescription()
    
class Pepperoni(Decorator):
    # carefully selected pepperonis to give a fine spicy taste
    cost = 2.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Meat(Decorator):
    # the finnest meat as toppings
    cost = 2.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Margherita(Decorator):
    # the classic, you won't regret it
    cost = 2.0
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Napoletana(Decorator):
    # the first of them all, Italy's most prized tradition
    cost = 2.25
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class QuattroFormaggi(Decorator):
    # four different cheese sprinkled on top, a specialty of the house
    cost = 2.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)

class Capricciosa(Decorator):
    # the name literally translates to capricious
    cost = 2.5
    def __init__(self, pizza_component):
        Decorator.__init__(self, pizza_component)


pizza1 = Pepperoni(Pizza())
print(pizza1.getDescription() + ": $" + str(pizza1.getCost()))
pizza2 = QuattroFormaggi(Meat(Pizza()))
print(pizza2.getDescription() + ": $" + str(pizza2.getCost()))
pizza3 = Capricciosa(Napoletana(Pizza()))
print(pizza3.getDescription() + ": $" + str(pizza3.getCost()))
