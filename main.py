from CreatePopulations import CreatePredatorPopulation, CreateVictimPopulation, victim_child, predator_child
from Settings import victim_population, predator_population
from Predator import *
from Victim import *
#############################
# 1) GENERATING POPULATIONS:#
#############################

predator_population = CreatePredatorPopulation(predator_population)
victim_population = CreateVictimPopulation(victim_population)

#############################
# 2) MAIN LOOP:         #####
#############################

#TO DO: mainloop, hunting, hybrydyzation, mutation...