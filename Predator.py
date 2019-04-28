from Animal import *
from Settings import victim_population, predator_population

class Predator(Animal):
    def __init__(self, strength, speed, attractiveness, gender):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    def Hunting(self):
        which_victim = randint(0, len(victim_population))
        victim = victim_population[which_victim]
        list_of_strength = sorted(predator_population, key=attrgetter('strength'))
        alpha_predator = list_of_strength[0]
        if(alpha_predator.speed > victim.speed):
            hidden_victim = victim.Hide()
            if(hidden_victim == True):
                return False
            else:
                return True