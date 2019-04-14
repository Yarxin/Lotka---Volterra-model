from Animal import *

class Victim(Animal):

    def __init__(self, speed, attractiveness, gender, satiety):
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender
        self.satiety = satiety

    def Hide(self):
        pass