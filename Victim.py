from Animal import *

class Victim(Animal):
    def __init__(self, strength, speed, attractiveness, gender):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    def Hide(self):
        pass