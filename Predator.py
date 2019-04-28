from Animal import *
from Settings import victim_population, predator_population

class Predator(Animal):
    def __init__(self, strength, speed, attractiveness, gender):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    @staticmethod
    def Hunting(vitality, vict_popul):
        number_of_victims = len(vict_popul)
        number_of_victims = number_of_victims - 1
        which_victim = randint(0, number_of_victims)
        alpha_mistake = randint(1, 10)
        victim = victim_population[which_victim]
        list_of_strength = sorted(predator_population, key=attrgetter('strength'))
        alpha_predator = list_of_strength[0]
        if(alpha_predator.speed > victim.speed):
            hidden_victim = victim.Hide()
            if(alpha_mistake <= 3):
                vitality -= 1
                return vitality
            elif(hidden_victim == True):
                vitality -= 1
                return vitality
            else:
                Animal.Die(victim_population, victim)
                vitality = 3
                return vitality
        else:
            vitality -= 1
            return vitality