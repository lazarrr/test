import random

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
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


class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
    def __str__(self):
        return f"Dice with {self.sides} sides"

    def __repr__(self):
        return f"Dice({self.sides})"

    def is_fair(self):
        return self.sides >= 2