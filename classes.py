
class Dog:

    def __init__(self, name):
        self.name = name

    def talk(self): # def f(x):
        print(f"{self.name} says woof!")

# timeline
jojo = Dog("jojo") # jojo is born
chocolate = Dog("chocolate") # chocolate is born

jojo.talk() 
chocolate.talk()
