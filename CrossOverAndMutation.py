
import Classes
import SelectionProcess
import random
import SetTime


def crossOver(population = Classes.Population()):



    parent1 = SelectionProcess.tournamentSelection(population)
    parent2 = SelectionProcess.tournamentSelection(population)

    #print("Parent 1 original fitness ",parent1.fitness)
    #print("Parent 2 original fitness ",parent2.fitness)

    randomNumbers = generateRandomNumber(parent1.geneList.__len__())

    Children = []

    '''
    swapping whole gene // bad idea 
    
    for x in range(randomNumbers.__len__()):

        rd = randomNumbers[x]

        temp = parent1.geneList[rd]
        parent1.geneList[rd] = parent2.geneList[rd]
        parent2.geneList[rd] = temp

    '''

    Children = crossOverAgainstTime(parent1,parent2)
    Children = crossOverAgainstDay(Children[0], Children[1])
    Children = crossOverAgainstRoom(Children[0],Children[1])

    Children = MutationAgainstRoom(Children[0],Children[1])
    Children = MutationAgainstDay(Children[0],Children[1])
    Children = MutationAgainstTime(Children[0],Children[1])

    return Children




def crossOverAgainstDay(parent1,parent2):

    randomNumbers = generateRandomNumber(10)

    for x in range(randomNumbers.__len__()):

        rd = randomNumbers[x]

        temp_day = parent1.geneList[rd].Day
        parent1.geneList[rd].Day = parent2.geneList[rd].Day
        parent2.geneList[rd].Day = temp_day

    return [parent1, parent2]


def crossOverAgainstTime(parent1, parent2):
    randomNumbers = generateRandomNumber(30)

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
    randomNumbers = generateRandomNumber(6)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        Room = parent1.geneList[rd].Room


        parent1.geneList[rd].Room = parent2.geneList[rd].Room


        parent2.geneList[rd].Room = Room

    return[parent1,parent2]



def generateRandomNumber(size):

    randomNumbers = []
    size = size/2
    size = int(size)
    for x in range(size):

        repeat = True
        num = random.randint(0,size-1)

        while(repeat):
            if(num not in randomNumbers):
                randomNumbers.append(num)
                repeat = False

            else:
                num = random.randint(0, size - 1)


    return randomNumbers




def MutationAgainstRoom(child1,child2):


    randomNumbers = generateRandomNumber(10)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        #class
        if(child1.geneList[rd].Type==0):

            child1.geneList[rd].Room = random.randint(2, 6)

        #lab
        elif(child1.geneList[rd].Type==1):

            child1.geneList[rd].Room = random.randint(0, 1)



    randomNumbers = generateRandomNumber(10)

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


    randomNumbers = generateRandomNumber(30)

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


    randomNumbers = generateRandomNumber(10)

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
    randomNumbers = generateRandomNumber(10)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        child1.geneList[rd].Day = random.randint(0,4)

    randomNumbers = generateRandomNumber(10)

    for x in range(randomNumbers.__len__()):
        rd = randomNumbers[x]

        child1.geneList[rd].Day = random.randint(0, 4)

    return [child1, child2]

