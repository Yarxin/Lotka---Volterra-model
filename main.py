from Animal import *
from Predator import *
from Victim import *
from CreatePopulations import *
from Settings import *

#############################
# 1) GENERATING POPULATIONS:#
#############################
predator_population = []
victim_population = []

predator_population = CreatePredatorPopulation(predator_population)
victim_population = CreateVictimPopulation(victim_population)

#############################
# 2) MAIN LOOP:         #####
#############################

#TO DO: mainloop, hunting, hybrydyzation, mutation...