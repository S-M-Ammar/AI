import PrintFunctions
import PopulationGenerator
import SelectionProcess
import PrintFunctions
import CrossOverAndMutation
import Fitness
import ProduceNewGeneration
import Classes

population = PopulationGenerator.GeneratePopulation()
#PrintFunctions.printPopulation(population)

chr = Classes.Chromosome
flag = False
i = 1
while(flag==False):

    print("\n\n\n\n")

    population = ProduceNewGeneration.produceGeneration(population)
    #PrintFunctions.printPopulation(population)

    for x in population.chromosomeList:

        if(x.fitness>=-10):
            PrintFunctions.printPopulation(population)
            chr = x
            flag = True
            break

    i=i+1

    if(flag==True):
        break

print(Fitness.CalculateFitness(chr))




'''
print("\n\n\n\n")

population = ProduceNewGeneration.produceGeneration(population)
PrintFunctions.printPopulation(population)

print("\n\n\n\n")

population = ProduceNewGeneration.produceGeneration(population)
PrintFunctions.printPopulation(population)

#PrintFunctions.printChromosome(newChilds[0])


'''





