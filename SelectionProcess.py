import Classes
import random

# using tournament selection

#tournament selector is not fixed. It will variate with respect to process (as flow goes on...)

def tournamentSelection(population = Classes.Population()):

    #k =  random.randint(3,population.chromosomeList.__len__()-3)
    k = 2

    candidate_List = []

    for x in range(k):

        z = random.randint(0,population.chromosomeList.__len__()-3)
        candidate_List.append(population.chromosomeList[z])

    winner = candidate_List[0]

    for x in candidate_List:

        if(x.fitness > winner.fitness):
            winner = x


    return winner