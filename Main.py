import Fitness
import PopulationGenerator
import PrintFunctions
import ProduceNewGeneration
import Classes

population = PopulationGenerator.GeneratePopulation()


chr = Classes.Chromosome
flag = False
i = 1
gn = 1
while(flag==False):

    print("\n\n\n\n")
    print("Generation # ",gn,"\n")
    population = ProduceNewGeneration.produceGeneration(population)
    PrintFunctions.printPopulation(population)
    population.populationLimit = population.chromosomeList.__len__()
    gn = gn + 1



    for x in population.chromosomeList:

        if(x.fitness>10):

            chr = x
            PrintFunctions.printChromosome(chr)
            flag = True
            break

    i=i+1

    if(flag==True):

       break



fit = Fitness.CalculateFitness(chr)
'''
for x in population.chromosomeList:
    if(x.fitness==0):
        PrintFunctions.printChromosome(x)
        fit = Fitness.CalculateFitness(chr)

        print(x.fitness)
        print("\n\n\n")

'''



'''
print("\n\n\n\n")

population = ProduceNewGeneration.produceGeneration(population)
PrintFunctions.printPopulation(population)

print("\n\n\n\n")

population = ProduceNewGeneration.produceGeneration(population)
PrintFunctions.printPopulation(population)

#PrintFunctions.printChromosome(newChilds[0])


'''





