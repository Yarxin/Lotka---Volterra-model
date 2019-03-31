from Animal import *

class Victim(Animal):

    def __init__(self, hp, speed, attractiveness, gender, satiety):
        self.hp = hp
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender
        self.satiety = satiety

    def Hide(self):
        pass