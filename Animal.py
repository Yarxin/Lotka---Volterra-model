import numpy as np
from Settings import victim_population, predator_population
from operator import attrgetter
from random import *

class Animal:
    def __init__(self, strength, speed, attractiveness, gender):
        self.strength = strength
        self.speed = speed
        self.attractiveness = attractiveness
        self.gender = gender

    @staticmethod
    def PickMaleAlphaParent(popul_list):
        ###using ranking method###
        sorted(popul_list, key=attrgetter('strength'))
        for index, individual in enumerate(popul_list):
            if(individual[index].gender == 1):
                alpha_male = individual[index]
        return alpha_male

    @staticmethod
    def PickFemaleParent(popul_list):
        ###using rulet method###
        adaptation_sum = 0
        end_condition = 0
        rulet_field = randint(1, 10)
        for index, individual in popul_list:
            if(individual.gender == 0):
                adaptation_sum += individual.strength
        end_condition = randint(1, adaptation_sum)
        i = 0
        while(end_condition <= rulet_field):
            if(popul_list[i].gender == 0):
                end_condition += popul_list[i].strength
            i += 1
        female_parent = popul_list[i]
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
            child.attractiveness = parentMale.attracticeness
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
        pass

    def Die(self):
        pass

