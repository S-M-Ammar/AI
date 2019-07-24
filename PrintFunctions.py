import Classes
import CodeList

def printChromosome(chromosome1 = Classes.Chromosome()):

    print("\n\n")
    for x in chromosome1.geneList:
        print( CodeList.code_Subject[x.CourseID],"   ",CodeList.code_Teacher[x.Teacher],"   ",CodeList.Section[x.Section],"   ",CodeList.class_type[x.Type],"   ",CodeList.Batch[x. Batch],"   ",CodeList.Room[x.Room],"   ",x.start_time,"   ",x.end_time,"   ",CodeList.Day[x.Day])
        print("\n")

    print("\n\n\n")


def printPopulation(population=[]):
    i = 1
    for x in population.chromosomeList:
        print("Chromosome # ", i, "\tfitness = ", x.fitness)
        i = i + 1
