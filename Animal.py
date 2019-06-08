import numpy as np
from Settings import victim_population, predator_population
from operator import attrgetter
from random import *
import random
import copy

class Animal:
    def __init__(self, strength, speed, attractiveness, gender, age):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    @staticmethod
    def PickMaleAlphaParent(popul_list):
        ###using ranking method###
        sorted(popul_list, key=attrgetter('strength'))
        for index, individual in enumerate(popul_list):
            if(individual.gender == 1):
                alpha_male = popul_list[index]
                break
            else:
                gender_corector = randint(0, len(popul_list) - 1)
                popul_list[gender_corector].gender = 1
                alpha_male = popul_list[gender_corector]
        return alpha_male


    @staticmethod
    def PickFemaleParent(popul_list):
        ###using rulet method###
        adaptation_sum = 0
        end_condition = 0
        work_popul = copy.copy(popul_list)
        for individual in popul_list:
            if(individual.gender == 0):
                adaptation_sum += individual.attractiveness

        i = 0
        rulet_field = random.uniform(0, adaptation_sum)
        while(end_condition < rulet_field):
            if(work_popul[i].gender == 0):
                end_condition += work_popul[i].attractiveness
            i += 1
        female_parent = work_popul[i -1]
        return female_parent

    @staticmethod
    def Hybrydization(parentMale, parentFemale, child):
        which_parent = randint(0, 1)
        ###
        if (which_parent == 1):
            child.strength = parentMale.strength
            which_parent = randint(0, 1)
        else:
            child.strength = parentFemale.strength
            which_parent = randint(0, 1)
        ###
        if (which_parent == 1):
            child.speed = parentMale.speed
            which_parent = randint(0, 1)
        else:
            child.speed = parentFemale.speed
            which_parent = randint(0, 1)
        ###
        if (which_parent == 1):
            child.attractiveness = parentMale.attractiveness
            which_parent = randint(0, 1)
        else:
            child.attractiveness = parentFemale.attractiveness
            which_parent = randint(0, 1)
        ###
        if (which_parent == 1):
            child.gender = parentMale.gender
        else:
            child.gender = parentFemale.gender
        return child

    @staticmethod
    def Mutation(child):
        #Chances as big as scientific literature says
        mut_prob = randint(1, 100)
        up_margin = 0.6
        down_margin = 1.7
        mutation = random.uniform(up_margin, down_margin)
        if(mut_prob == 1):
            mut_prob = randint(1, 3)
            if(mut_prob == 1):
                child.strength = child.strength * mutation
            elif(mut_prob == 2):
                child.speed = child.speed * mutation
            else:
                child.attractiveness = child.attractiveness * mutation
        #Gender doesn't mutate. Generally it doesn't :/
    @staticmethod
    def Die(anim_list, individual):
        anim_list.remove(individual)

        #anim_list - lista z populacją ofiar lub drapieżników

        #individual - osobnik do usunięcia z populacji

