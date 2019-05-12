from Animal import *

class Victim(Animal):
    def __init__(self, strength, speed, attractiveness, gender, age):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender
        self.age = age

    def Hide(self):
        hide_prob = randint(1, 10)
        if(hide_prob >= 2):
            return True
        else:
            return False