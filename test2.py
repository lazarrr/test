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
    
    def new_method(self):
        print("This is a new method in the Car class.")
        print("It can do something different.")
        print("You can call it like this:")
        return "New method executed."
    
  
    
class Dice:

    def __init__(self):
        self.sides = 6

    def __str__(self):
        return f"Dice with {self.sides} sides"

    def roll(self):
        print(f"Rolling a {self.sides}-sided dice...")
        return random.randint(1, self.sides)