# High cohesion in Python class 

class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

class UserActions:
    def __init__(self):
        self._phrase = "My name is {name} and I am {age} years old"

    def tell_phrase(self, user):
        print(self._phrase.format(name=user.name, age=user.age))


user = User(name="John", age=25)
actions_provider = UserActions()
actions_provider.tell_phrase(user)