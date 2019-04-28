from CreatePopulations import CreatePredatorPopulation, CreateVictimPopulation, victim_child, predator_child
from Settings import victim_population, predator_population, DAYS, SATIETY, MIN_SATIETY, VITALITY, AREA, PREDATOR_QUANTITY, VICTIM_QUANTITY, YEARS
from Predator import *
from Victim import *
from matplotlib import pyplot as plt
#############################
# 1) GENERATING POPULATIONS:#
#############################

predator_population = CreatePredatorPopulation(predator_population)
victim_population = CreateVictimPopulation(victim_population)

predator_statistics = []
predator_statistics.append(PREDATOR_QUANTITY)

victim_statistics = []
victim_statistics.append(VICTIM_QUANTITY)

current_year_predator_quantity = 0
current_year_victim_quantity = 0

years = []
timeline = 0
years.append(timeline)

#############################
# 2) MAIN LOOP:         #####
#############################
i = 0
wheel_of_fortune = 0

while(i <= DAYS):
    if(len(predator_population) == 0):
        print('All predators are dead.')
        break
    if(len(victim_population) == 0):
        print('All victims are dead.')
    # Checking if there is no overpopulation of victims.
    victim_satiety = AREA / len(victim_population)
    if(victim_satiety < MIN_SATIETY):
        wheel_of_fortune = randint(0, len(victim_population) - 1)
        Animal.Die(victim_population, victim_population[wheel_of_fortune])

    # Killing predators when the hunting goes bad :/
    predator_vitality = VITALITY
    if(VITALITY == 0):
        wheel_of_fortune = randint(0, len(predator_population) - 1)
        Animal.Die((predator_population, predator_population[wheel_of_fortune]))

    # Hunting time >:) once for every three days.
    if((i % 15) == 0):
        predator_vitality = Predator.Hunting(predator_vitality, victim_population)

    # Procreation once a year.
    if((i % 365) == 0):
        # How many children in victim population do we welcome this year?
        procreation_iterator = 0
        wheel_of_fortune = randint(1, 15)

        victim_male_parent = Animal.PickMaleAlphaParent(victim_population)
        while(procreation_iterator <= wheel_of_fortune):
            victim_female_parent = Animal.PickFemaleParent(victim_population)

            victim_newborn = Animal.Hybrydization(victim_male_parent, victim_female_parent, victim_child)
            Animal.Mutation(victim_newborn)
            victim_population.append(victim_newborn)
            procreation_iterator += 1

        # How many childern in predator population do we welcome this year?
        wheel_of_fortune = randint(1, 3)
        procreation_iterator = 0
        predator_male_parent = Animal.PickMaleAlphaParent(predator_population)
        while(procreation_iterator <= wheel_of_fortune):
            predator_female_parent = Animal.PickFemaleParent(predator_population)

            predator_newborn = Animal.Hybrydization(predator_male_parent, predator_female_parent, predator_child)
            Animal.Mutation(victim_newborn)
            predator_population.append(predator_newborn)
            procreation_iterator += 1

        # preparing statistics
        current_year_predator_quantity = len(predator_population)
        current_year_victim_quantity = len(victim_population)

        predator_statistics.append(current_year_predator_quantity)
        victim_statistics.append(current_year_victim_quantity)
        timeline += 1

        years.append(timeline)


    i += 1
plt.plot(years, predator_statistics)
plt.plot(years, victim_statistics)
plt.show()


# TO DO:
# ADD AGE TO PREDATORS AND START KILLING THE OLDEST
# ONE VICTIM CAN'T GIVE VITALITY TO MORE THAN  7 PREDATORS