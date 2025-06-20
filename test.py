import random

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is speaking.")
        return f"{self.name} makes a sound."

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def honk(self):
        return f"{self.brand} car honks!"

    def get_info(self):
        print(f"Getting info for {self.brand} car from {self.year}")
        print("This is a car object.")
        print("It has a brand and a year.")
        return f"{self.brand} {self.year}"
        return f"{self.year} {self.brand}"


    def new_method(self):
        print("This is a new method in the Car class.")
        print("It can do something different.")
        print("You can call it like this:")
        return "New method executed."


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        print(f"Rolling a {self.sides}-sided dice...")
        return random.randint(1, self.sides)
    
    def __str__(self):
        return f"Dice with {self.sides} sides"

    def __repr__(self):
        return f"Dice({self.sides})"

    def is_fair(self):
        print("Checking if the dice is fair...")
        return self.sides >= 2
    

def main():
    animal = Animal("Dog")
    print(animal.speak())

    car = Car("Toyota", 2020)
    print(car.honk())
    print(car.get_info())




    dice = Dice()
    print(dice.roll())
    print(dice)
    print(repr(dice))
    print(f"Is the dice fair? {dice.is_fair()}")


def test():
    animal = Animal("Cat")
    assert animal.speak() == "Cat makes a sound."

    car = Car("Honda", 2019)
    assert car.honk() == "Honda car honks!"
    assert car.get_info() == "Honda 2019"
    assert car.new_method() == "New method executed."

    dice = Dice(10)
    assert dice.roll() in range(1, 11)
    assert str(dice) == "Dice with 10 sides"

    assert repr(dice) == "Dice(10)"
    assert dice.is_fair() is True
