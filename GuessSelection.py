import Classes
import random


def randomSelectionProcess(population = Classes.Population()):


    size = population.chromosomeList.__len__()

    parent1_index = random.randrange(0,size-1)

    parent = population.chromosomeList[parent1_index]

    return parent

