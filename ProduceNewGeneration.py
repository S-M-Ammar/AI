import Classes
import Fitness
import CrossOverAndMutation

def produceGeneration(population = Classes.Population()):

    new_population = Classes.Population()

    for x in range( population.populationLimit ):

        newChild = CrossOverAndMutation.crossOver(population)

        Fit = Fitness.CalculateFitness(newChild)
        newChild.fitness = (Fit[0] + Fit[1] + Fit[2]) * -1


        new_population.chromosomeList.append(newChild)


    return new_population



