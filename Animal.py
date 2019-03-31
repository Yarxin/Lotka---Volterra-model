import numpy as np

class Animal:
    def __init__(self, hp, speed, attractiveness, gender):
        self.hp = hp
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    @staticmethod
    def PickParent():
        #using roulet method
        pass

    @staticmethod
    def Hybrydization(parentMale, parentFemale):
        pass

    @staticmethod
    def Mutation(child):
        pass

    def Die(self):
        pass

