from Animal import *

class Predator(Animal):
    def __init__(self, hp, speed, attractiveness, gender, vitality):
        self.hp = hp
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender
        self.vitality = vitality

    def Hunting(self):
        pass
