from Animal import *

class Victim(Animal):
    def __init__(self, strength, speed, attractiveness, gender):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    @staticmethod
    def Hybrydization(parentMale, parentFemale):
        which_parent = randint(0, 1)
        child = Victim(0, 0, 0, 0)
         ###
        if(which_parent == 1):
            child.strength = parentMale.strength
            which_parent = randint(0, 1)
        else:
            child.strength = parentFemale.strength
            which_parent = randint(0, 1)
         ###
        if(which_parent == 1):
            child.speed = parentMale.speed
            which_parent = randint(0, 1)
        else:
            child.speed = parentFemale.speed
            which_parent = randint(0, 1)
         ###
        if(which_parent == 1):
            child.attractiveness = parentMale.attracticeness
            which_parent = randint(0, 1)
        else:
            child.attractiveness = parentFemale.attractiveness
            which_parent = randint(0, 1)
         ###
        if(which_parent == 1):
            child.gender = parentMale.gender
        else:
            child.gender = parentFemale.gender

    def Hide(self):
        pass