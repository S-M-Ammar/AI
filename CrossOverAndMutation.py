import numpy as np
import Classes
import SelectionProcess
import random
import SetTime
import GuessSelection

def crossOver(population = Classes.Population()):

    parent1 = Classes.Chromosome()
    parent2 = Classes.Chromosome()

    parent1 = SelectionProcess.tournamentSelection(population)
    parent2 = SelectionProcess.tournamentSelection(population)

    #parent1 = GuessSelection.randomSelectionProcess(population)
    #parent2 = GuessSelection.randomSelectionProcess(population)

    #print("Parent 1 original fitness ",parent1.fitness)
    #print("Parent 2 original fitness ",parent2.fitness)

    #randomNumbers = generateRandomNumber(parent1.geneList.__len__())

    child = Classes.Chromosome()

    child = simpleCrossOver(parent1,parent2)


    return child


def simpleCrossOver(parent1=Classes.Chromosome() , parent2 = Classes.Chromosome()):

    child = Classes.Chromosome()

    for x in range(parent1.geneList.__len__()):

         z = np.random.random()

         if(z<=0.5):
             child.geneList.append(parent1.geneList[x])

         elif(z>0.5):
             child.geneList.append(parent2.geneList[x])

    return child

def simpleMutation(Child = Classes.Chromosome()):

    randomNumbers = generateRandomNumber(0,Child.geneList.__len__()-1,3)

    for x in randomNumbers:

        z = np.random.random()

        if(z<0.4):
            #Mutation Day

            Child.geneList[x].Day = random.randint(0,4)

        elif(z<0.7):
            #Mutation Time

            if (Child.geneList[x].Type == 0):

                timeList = SetTime.set_timing_for_class()

                Child.geneList[x].start_time = timeList[0]
                Child.geneList[x].end_time = timeList[1]

            # lab
            elif (Child.geneList[x].Type == 1):

                timeList = SetTime.set_timing_for_lab()

                Child.geneList[x].start_time = timeList[0]
                Child.geneList[x].end_time = timeList[1]




        elif(z<=1):
            #Mutation Room

            if (Child.geneList[x].Type == 0):

                Child.geneList[x].Room = random.randint(2, 6)

                # lab
            elif (Child.geneList[x].Type == 1):

                Child.geneList[x].Room = random.randint(0, 1)


    pass


def crossOverAgainstDay(parent1,parent2):

    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):

        rd = randomNumbers[x]

        temp_day = parent1.geneList[rd].Day
        parent1.geneList[rd].Day = parent2.geneList[rd].Day
        parent2.geneList[rd].Day = temp_day

    return [parent1, parent2]


def crossOverAgainstTime(parent1, parent2):
    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        start_time = parent1.geneList[rd].start_time
        end_time = parent1.geneList[rd].end_time

        parent1.geneList[rd].start_time = parent2.geneList[rd].start_time
        parent1.geneList[rd].end_time = parent2.geneList[rd].end_time

        parent2.geneList[rd].start_time = start_time
        parent2.geneList[rd].end_time = end_time

    return [parent1, parent2]


def crossOverAgainstRoom(parent1, parent2):
    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        Room = parent1.geneList[rd].Room


        parent1.geneList[rd].Room = parent2.geneList[rd].Room


        parent2.geneList[rd].Room = Room

    return[parent1,parent2]



def generateRandomNumber(startingRange,endingRange,size):

    randomNumbers = []

    for x in range(size):

        repeat = True
        num = random.randint(startingRange,endingRange)

        while(repeat):
            if(num not in randomNumbers):
                randomNumbers.append(num)
                repeat = False

            else:
                num = random.randint(startingRange,endingRange)


    return randomNumbers




def MutationAgainstRoom(child1,child2):


    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        #class
        if(child1.geneList[rd].Type==0):

            child1.geneList[rd].Room = random.randint(2, 6)

        #lab
        elif(child1.geneList[rd].Type==1):

            child1.geneList[rd].Room = random.randint(0, 1)



    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        #class
        if(child2.geneList[rd].Type==0):

            child2.geneList[rd].Room = random.randint(2, 6)

        #lab
        elif(child2.geneList[rd].Type==1):

            child2.geneList[rd].Room = random.randint(0, 1)


    return [child1,child2]



def MutationAgainstTime(child1, child2):


    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]


        # class
        if (child1.geneList[rd].Type == 0):

            timeList = SetTime.set_timing_for_class()

            child1.geneList[rd].start_time = timeList[0]
            child1.geneList[rd].end_time = timeList[1]

        # lab
        elif (child1.geneList[rd].Type == 1):

            timeList = SetTime.set_timing_for_lab()

            child1.geneList[rd].start_time = timeList[0]
            child1.geneList[rd].end_time = timeList[1]


    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        # class
        if (child2.geneList[rd].Type == 0):

            timeList = SetTime.set_timing_for_class()

            child2.geneList[rd].start_time = timeList[0]
            child2.geneList[rd].end_time = timeList[1]

        # lab
        elif (child2.geneList[rd].Type == 1):

            timeList = SetTime.set_timing_for_lab()

            child2.geneList[rd].start_time = timeList[0]
            child2.geneList[rd].end_time = timeList[1]

    return [child1,child2]

def MutationAgainstDay(child1,child2):
    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        child1.geneList[rd].Day = random.randint(0,4)

    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        child1.geneList[rd].Day = random.randint(0, 4)

    return [child1, child2]


def SwappingGene(child1,child2):

    randomNumbers = generateRandomNumber(0,23,6)

    for x in range(randomNumbers.__len__()):

        rd = randomNumbers[x]

        temp = child1.geneList[rd]
        child1.geneList[rd] = child2.geneList[rd]
        child2.geneList[rd] = temp
