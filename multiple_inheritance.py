class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def run(self):
        print(f"{self.name} is running fast")
class pest(Animal):
    def flee(self):
        print(f"{self.name} is fleeing from danger")

class predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting for food")

class Rabbit(pest):
    pass

class Snake(predator):
    pass

class Fish(pest,predator):
    def action(self):
        print(f"{self.color} {self.name} is swimming in the water")

predator = predator("Lion", "yellow")
predator.hunt()
rabbit = Rabbit("Bunny", "White")
snake = Snake("Slither", "Green")
fish = Fish("Nemo", "Goldfish")
#rabbit.run()
rabbit.flee()
fish.action()