import Classes
import ChromosomeGenrator
import GenerateTime


def GeneratePopulation():

    population = Classes.Population()
    population.populationLimit = 500
    Time_List = GenerateTime.takeTime()

    for x in range(population.populationLimit):

        population.chromosomeList.append(ChromosomeGenrator.GenerateChromosome(Time_List))

    return population









