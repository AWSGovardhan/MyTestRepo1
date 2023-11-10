# Low cohesion Python class example will look like :

class User:
    def __init__(self):
        self.name = None
        self.age = None
        self._phrase = "My name is {name} and I am {age} years old"

    def define_name_and_age(self, name, age):
        self.name = name
        self.age = age
    
    def send_mail_of_the_phrase(self, other_user):
        mail_client = MailClient()
        phrase = self.get_phrase()
        mail_client.send(phrase, to=other_user)

    def get_phrase(self):
        return self._phrase.format(name=self.name, age=self.age)

    def tell_phrase(self):
        print(self.get_phrase())


user = User()
user.tell_phrase()  # oops 'My name is None and I am None years old'
user.define_name_and_age(name="Alex", age=37)
user.tell_phrase()  # My name is Alex and I am 37 years old