from Predator import *
from Victim import *
from random import *
from Settings import *

############
# PREDATORS#
############
def GeneratePredator():
    pred_strength = randint(1, 10)
    pred_speed = randint(1, 10)
    pred_attractiveness = randint(1, 5)
    pred_gender = randint(0, 1)
    pred_vitality = randint(1, 3)

    predator = Predator(pred_strength, pred_speed, pred_attractiveness, pred_gender, pred_vitality)
    return predator

def CreatePredatorPopulation(pred_list):
    pred_iterator = 0
    while (pred_iterator <= PREDATOR_QUANTITY):
        pred_list.append(GeneratePredator())
        pred_iterator += 1
    return pred_list

##########
# VICTIMS#
##########
def GenerateVictim():
    vict_strength = randint(1, 10)
    vict_speed = randint(1, 10)
    vict_attractiveness = randint(1, 5)
    vict_gender = randint(0, 1)
    vict_satiety = VICTIM_QUANTITY/AREA

    victim = Victim(vict_strength, vict_speed, vict_attractiveness, vict_gender, vict_satiety)
    return victim

def CreateVictimPopulation(vict_list):
    vict_iterator = 0
    while (vict_iterator <= VICTIM_QUANTITY):
        vict_list.append(GenerateVictim())
        vict_iterator += 1
    return vict_list