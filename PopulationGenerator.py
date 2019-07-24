import Classes
import ChromosomeGenrator
import GenerateTime


def GeneratePopulation():

    population = Classes.Population()
    Time_List = GenerateTime.takeTime()

    for x in range(58):

        population.chromosomeList.append(ChromosomeGenrator.GenerateChromosome(Time_List))

    return population









