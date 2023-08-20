# Question 1:the Person class has a constructor that takes name and age as arguments and assigns them to the object's attributes. The introduce method is then invoked on the object to introduce the person.
class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
        
    def display_info(self):
        print(f"Name is {self.name} and age is {self.age}")

Jiten = Person("Jiten","28")
Jiten.display_info()

