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
    PrintFunctions.printPopulation(population)
    population.populationLimit = population.chromosomeList.__len__()

    for x in population.chromosomeList:

        if(x.fitness>=-4):
            #PrintFunctions.printPopulation(population)
            chr = x
            flag = True
            break

    i=i+1

    if(flag==True):
        break

for x in population.chromosomeList:
    if(x.fitness>=-4):
        PrintFunctions.printChromosome(x)
        print(x.fitness)
        print("\n\n\n")




'''
print("\n\n\n\n")

population = ProduceNewGeneration.produceGeneration(population)
PrintFunctions.printPopulation(population)

print("\n\n\n\n")

population = ProduceNewGeneration.produceGeneration(population)
PrintFunctions.printPopulation(population)

#PrintFunctions.printChromosome(newChilds[0])


'''





