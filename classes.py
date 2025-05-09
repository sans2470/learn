
class Dog:

    def __init__(self, name, dob): # attributes
        self.name = name
        self.dob = dob

    def talk(self): # def f(x):
        print(f"{self.name} says woof!")
    
    def tellmeDOB(self):
        print(f"{self.name} birthday is {self.dob}")

# timeline
jojo = Dog("jojo", "2022-01-01") # jojo is born
chocolate = Dog("chocolate", "2023-02-02") # chocolate is born

jojo.talk() 
chocolate.talk()

jojo.tellmeDOB()
chocolate.tellmeDOB()
