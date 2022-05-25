#!/usr/bin/python3
import random
import numpy

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

    def __init__(self, name="", number=0, typep="", height="", weight="", attack=0, score=0):
        self.name = name
        self.number = number
        self.typep = typep
        self.height = height
        self.weight = weight
        self.score = score
    
    def attack(self, attack):
        self.attack = attack 
        attack = random.randrange(0.0, 1.0)


