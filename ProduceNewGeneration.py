import Classes
import Fitness
import CrossOverAndMutation

def produceGeneration(population = Classes.Population()):

    new_population = Classes.Population()

    for x in range(29):

        newChilds = CrossOverAndMutation.crossOver(population)

        Fit = Fitness.CalculateFitness(newChilds[0])
        newChilds[0].fitness = (Fit[0] + Fit[1] + Fit[2]) * -1

        Fit = Fitness.CalculateFitness(newChilds[1])
        newChilds[1].fitness = (Fit[0] + Fit[1] + Fit[2]) * -1


        new_population.chromosomeList.append(newChilds[0])
        new_population.chromosomeList.append(newChilds[1])


    return new_population



