from Animal import *

class Victim(Animal):
    def __init__(self, strength, speed, attractiveness, gender, satiety):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender
        self.satiety = satiety

    def Hide(self):
        pass