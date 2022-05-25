#!/usr/bin/python3
import random
import math

"""
oop_challenge
Class Pokemon
"""
class Pokemon:

    """
    Attributes:
        name
        number
        typep
        height
        weight
        attack
        score

    Methods:
        attack
    """

    def __init__(self, name="", number=0, typep="", height="", weight="", health=0):
        self.name = name
        self.number = number
        self.typep = typep
        self.height = height
        self.weight = weight
        self.__health = health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        if health < 0:

            raise ValueError("Health must be more than 0")
        elif type(health) != int:
            raise TypeError("Health must be an integer")
        else:
            self.__health = health
    
    def attack(self, attack):
        self.attack = attack 
        attack = random.randrange(0.0, 1.0)

    def defense(self, defense):
        self.defense = defense
        defense = random.randrange(0.0, 1.0)

class Battle:
    def star_F(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        while True:
            if self.getAttackResult(pokemon1, pokemon2):
                break
            
        while True:
            if self.getAttackResult(pokemon2, pokemon1):
                break

    @staticmethod
    def getAttackResult(pokemon1, pokemon2):
        pokemon1attack = pokemon1.attack()
        pokemon2defense = pokemon2.defense()
        if pokemon2defense - pokemon1attack > 0:
            print("DODGE ATTACK!")
        else:
            damage2pokemon2 = math.ceil(pokemon1attack - pokemon2defense)
            pokemon2.health = pokemon2.health - damage2pokemon2

        if pokemon2.health <= 0:
            return()

        else:
            return()

pokemonC = Pokemon("Charizard", 6, "Fire", "1.54m", "100kg", 5)
pokemonM = Pokemon("Mewtwo", 150, "Psychic", "1.87m", "135Kg", 7)
print(pokemonC)
print(pokemonM)
fight1 = Battle(pokemonC, pokemonM)
a = Pokemon(pokemonC)
print(a)