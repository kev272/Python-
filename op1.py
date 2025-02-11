class Person:
    def __init__(self, name, age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def speak(self):
        print(self.name,"Is speaking" )

Person1 = Person("John",24,"Teacher")
print(Person1.name)

Person2 = Person("Mary",24,"Doctor")
print(Person2.name)
Person2.speak()