#Creational Pattern ==> Builder Pattern

class Burger:
    def __init__(self):
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self,bunStyle):
        self.buns = bunStyle

    def setPatty(self,pattyStyle):
        self.patty = pattyStyle

    def setCheese(self,cheeseStyle):
        self.cheese = cheeseStyle

class BurderBuilder:
    def __init__(self):
        self.burger = Burger()

    def addBun(self,bunStyle):
        self.burger.setBun(bunStyle)
        return self
    
    def addPatty(self,pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self
    
    def addCheese(self,cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self
    
    def build(self):
        return self.burger;

b1 = BurgerBuilder()\
    .addBun("seseme")\
    .addCheese("Veg-patty")\
        .addCheese('Swiss Cheese')\
            .build()

