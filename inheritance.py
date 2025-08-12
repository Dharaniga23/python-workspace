class Birds:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def fly(self):
        print(f"{self.name} is flying in the sky")
    def eat(self):
        print(f"{self.name} is eating seeds")

class peacock(Birds):
   # peacock = Birds("kyy", "Blue")
   # peacock.fly()
    def speak(self):
        print(f"{peacock.name} is making a woof sound")
class parrot(Birds):
   # parrot = Birds("keekee ", "Green")
   # parrot.eat()
    def speak(self):
        print(f"{parrot.name} is making a woof sound")

peacock = peacock("kyy", "Blue")
parrot = parrot("keekee", "Green")
peacock.fly()
peacock.speak()
parrot.eat()
parrot.speak()