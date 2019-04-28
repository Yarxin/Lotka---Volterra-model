from Animal import *

class Victim(Animal):
    def __init__(self, strength, speed, attractiveness, gender):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    def Hide(self):
        hide_prob = randint(1, 10)
        if(hide_prob >= 7):
            return True
        else:
            return False