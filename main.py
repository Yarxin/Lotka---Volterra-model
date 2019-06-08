from CreatePopulations import CreatePredatorPopulation, CreateVictimPopulation, victim_child, predator_child, GeneratePredator
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

mean_speed_vict = []
mean_speed_pred = []
mean_speed_pred.append(0)
mean_speed_vict.append(0)

max_speed_vict = []
max_speed_pred = []

years = []
timeline = 0
years.append(timeline)

predator_vitality = VITALITY

#############################
# 2) MAIN LOOP:         #####
#############################
i = 0
wheel_of_fortune = 0

while(i <= DAYS):
    print(i)
    environment_resistance = len(victim_population) / AREA
    if(len(predator_population) == 0):
        print('All predators are dead.')
        break
    if(len(victim_population) == 0):
        print('All victims are dead.')
    # Checking if there is no overpopulation of victims.
    #victim_satiety = AREA / len(victim_population)

    # Killing predators when the hunting goes bad :/
    # predator_vitality = VITALITY
    if(predator_vitality == 0):
        wheel_of_fortune = randint(0, len(predator_population) - 1)
        Animal.Die(predator_population, predator_population[wheel_of_fortune])

    # Hunting time >:)
    # Need to check if there are proper quantity of victims
    if(environment_resistance < 0.5):
        # if it is:
        if((i % 3) == 0):
            if(len(predator_population) > 5):
                hunt = 0
                while (hunt <= 2):
                    predator_vitality = Predator.Hunting(predator_vitality, victim_population)
                    hunt += 1
            else:
                predator_vitality = Predator.Hunting(predator_vitality, victim_population)
    else:
        for pred in predator_population:
            predator_vitality = Predator.Hunting(predator_vitality, victim_population)

    if((i % 365) == 0):

        # Killing the oldest
        for victim in victim_population:
            victim.age += 1
            if (victim.age == 6):
                Animal.Die(victim_population, victim)

        for predator in predator_population:
            predator.age += 1
            if (predator.age == 8):
                Animal.Die(predator_population, predator)

        # Procreation once a year.
        # How many children in victim population do we welcome this year?
        # 1 - 15 real numbers of children in Stag's population.
        procreation_iterator = 0
        # environment_resistance = len(victim_population) / AREA

        if(environment_resistance < 0.5):
            wheel_of_fortune = randint(1, 15)
            # print('rozmnażanie wariant A')
        # but if it's getting to much of victims?
        else:
            # wheel_of_fortune = randint(1, 2)
            wheel_of_fortune = 0
            # print('rozmnażanie wariant B')

        #To procreate Stags, we need to point the Daddy
        victim_male_parent = Animal.PickMaleAlphaParent(victim_population)

        while(procreation_iterator < wheel_of_fortune):
            #and mommy
            victim_female_parent = Animal.PickFemaleParent(victim_population)

            victim_newborn = Animal.Hybrydization(victim_male_parent, victim_female_parent, victim_child)
            Animal.Mutation(victim_newborn)
            victim_population.append(victim_newborn)
            procreation_iterator += 1

        # How many childern in predator population do we welcome this year?
        wheel_of_fortune = randint(1, 3) # Normal number of newborns in woolf's pack
        procreation_iterator = 0
        predator_male_parent = Animal.PickMaleAlphaParent(predator_population)
        while(procreation_iterator <= wheel_of_fortune):
            predator_female_parent = Animal.PickFemaleParent(predator_population)

            predator_newborn = Animal.Hybrydization(predator_male_parent, predator_female_parent, predator_child)
            Animal.Mutation(victim_newborn)
            wheel_of_fortune = randint(1, 5)
            predator_population.append(predator_newborn)
            if (wheel_of_fortune != 5):
                Animal.Die(predator_population, predator_newborn)
            procreation_iterator += 1


        # Natural process of leaving the pack
        if(len(predator_population) > 10):
            go_away = 0
            while(len(predator_population) > 5):
                go_away = randint(0, len(predator_population) - 1)
                Animal.Die(predator_population, predator_population[go_away])
            # WELCOME NEW ONE FROM FAR FAR AWAY
            predator_population.append(GeneratePredator())

        # preparing statistics
        current_year_predator_quantity = len(predator_population)
        current_year_victim_quantity = len(victim_population)

        predator_statistics.append(current_year_predator_quantity)
        victim_statistics.append(current_year_victim_quantity)
        timeline += 1

        mean_vc_sp = 0
        mean_pr_sp = 0
        for index, vc in enumerate(victim_population):
            mean_vc_sp += victim_population[index].speed
        mean_vc_sp = mean_vc_sp / len(victim_population)

        for index, pr in enumerate(predator_population):
            mean_pr_sp += predator_population[index].speed
        mean_pr_sp = mean_pr_sp / len(predator_population)

        mean_speed_vict.append(mean_vc_sp)
        mean_speed_pred.append(mean_pr_sp)

        years.append(timeline)

        # print('Liczebność populacji ofiar:' + str(len(victim_population)))
        # print('Obszar' + str(AREA))
        # print('opór środowiska = ' + str(environment_resistance))
    i += 1

plt.plot(years, predator_statistics, label='drapieżnicy')
plt.plot(years, victim_statistics, label='ofiary')
plt.grid(color='black', linestyle='-', linewidth=0.2)
plt.xlabel('Czas [lata]')
plt.ylabel('Liczebność populacji')
plt.title('Przebieg zmian liczebnosci ofiar i drapieżników w funkcji czasu')
plt.legend()
plt.show()

plt.subplot(2, 1, 1)
plt.plot(years, mean_speed_pred)
plt.grid(color='black', linestyle='-', linewidth=0.2)
plt.xlabel('Czas [lata]')
plt.ylabel('wartość średniego przystosowania')
plt.title('Funkcja przystosowania średniego cechy drapieżników: prędkość')

plt.subplot(2, 1, 2)
plt.plot(years, mean_speed_vict)
plt.grid(color='black', linestyle='-', linewidth=0.2)
plt.xlabel('Czas [lata]')
plt.ylabel('wartość średniego przystosowania')
plt.title('Funkcja przystosowania średniego cechy ofiar: prędkość')
plt.show()
