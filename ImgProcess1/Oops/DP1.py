class Burger:
    def __init__(self,ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


#Factory Pattern
class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ['bun','cheese','veg-patty',]
        return Burger(ingredients)

    def createVeganCheeseBurger(self):
        ingredients = ['bun','cheese','lettuce','veg-patty']
        return Burger(ingredients)
    
    def createDeluxeVeganCheeseBurger(self):
        ingredients = ['bun','cheese','lettuce','tomato','chicken-patty']
        return Burger(ingredients)

burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createVeganCheeseBurger().print()
burgerFactory.createDeluxeVeganCheeseBurger().print()
