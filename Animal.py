import numpy as np
from Settings import victim_population, predator_population
from operator import attrgetter
from random import *
import random

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
                alpha_male = popul_list[0]
        return alpha_male


    @staticmethod
    def PickFemaleParent(popul_list):
        ###using rulet method###
        adaptation_sum = 0
        end_condition = 0
        for individual in popul_list:
            if(individual.gender == 0):
                adaptation_sum += individual.strength

        i = 0
        rulet_field = random.uniform(0, adaptation_sum)
        while(end_condition < rulet_field):
            if(popul_list[i].gender == 0):
                end_condition += popul_list[i].strength
            i += 1
        female_parent = popul_list[i -1]
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
        mut_prob = randint(1, 3)
        up_margin = 0.6
        down_margin = 1.7
        mutation = random.uniform(up_margin, down_margin)
        if(mut_prob == 3):
            mut_prob = randint(1, 3)
            if(mut_prob == 1):
                child.strength = child.strength * mutation
            elif(mut_prob == 2):
                child.speed = child.speed * mutation
            else:
                child.attractiveness = child.attractiveness * mutation
        #Płeć nie podlega mutacji. Zazwyczaj nie podlega :/

    @staticmethod
    def Die(anim_list, individual):
        anim_list.remove(individual)

        #anim_list - lista z populacją ofiar lub drapieżników

        #individual - osobnik do usunięcia z populacji

