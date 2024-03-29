import numpy as np
import Classes
import SelectionProcess
import random
import SetTime
import GuessSelection
import RouletteSelection

def crossOver(population = Classes.Population()):

    parent1 = Classes.Chromosome()
    parent2 = Classes.Chromosome()

    parent1 = SelectionProcess.tournamentSelection(population)
    parent2 = SelectionProcess.tournamentSelection(population)

    #parent1 = RouletteSelection.RouletteWheelSelection(population)
    #parent2 = RouletteSelection.RouletteWheelSelection(population)


    #parent1 = GuessSelection.randomSelectionProcess(population)
    #parent2 = GuessSelection.randomSelectionProcess(population)

    #print("Parent 1 original fitness ",parent1.fitness)
    #print("Parent 2 original fitness ",parent2.fitness)

    #randomNumbers = generateRandomNumber(parent1.geneList.__len__())

    child = Classes.Chromosome()


    #child = CrossOverAndMutation(parent1,parent2)
    #child = mate(parent1,parent2)
    child = simpleCrossOver(parent1,parent2)
    #print(child.geneList.__len__());
    #child = simpleCrossOver(parent1,parent2)
    #child = simpleMutation(child)


    return child

def mate(par1, par2):

        child = Classes.Chromosome()

        scale = int((par1.geneList.__len__() )/ 4)

        for x in range(0, scale):
            child.geneList.append(par1.geneList[x])

        for x in range(scale, scale+scale):
            child.geneList.append(par2.geneList[x])

        for x in range(scale+scale , scale+scale+scale):
            child.geneList.append(par1.geneList[x])

        for x in range(scale+scale+scale, par1.geneList.__len__()):
            child.geneList.append(par2.geneList[x])



        mutationChance = random.random()


        for x in range(1):

                type_same = 0

                while(type_same!=1):
                    firstHalf = int(child.geneList.__len__() / 2)
                    secondHalf = firstHalf+1
                    index1 = random.randint(0,firstHalf)
                    index2 = random.randint(secondHalf,child.geneList.__len__()-1)

                    if(child.geneList[index1].Type == child.geneList[index2].Type):
                        type_same = 1
                        Day = child.geneList[index2].Day
                        Room = child.geneList[index2].Room
                        start_time = child.geneList[index2].start_time
                        end_time = child.geneList[index2].end_time


                        child.geneList[index2].Day = child.geneList[index1].Day
                        child.geneList[index2].Room = child.geneList[index1].Room
                        child.geneList[index2].start_time = child.geneList[index1].start_time
                        child.geneList[index2].end_time = child.geneList[index1].end_time

                        child.geneList[index1].Day = Day
                        child.geneList[index1].Room = Room
                        child.geneList[index1].start_time = start_time
                        child.geneList[index1].end_time = end_time




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

def CrossOverAndMutation(parent1=Classes.Chromosome() , parent2 = Classes.Chromosome()):

    child = Classes.Chromosome()

    for x in range(parent1.geneList.__len__()):

        z = random.random()

        if (z <= 0.5):
            child.geneList.append(parent1.geneList[x])

        elif (z<=0.9):
            child.geneList.append(parent2.geneList[x])

        else:

            child.geneList.append(parent1.geneList[x])
            k =np.random.random()


            if(k<=0.32):
                child = mutationAgainstDay(child,x)
                pass


            elif(k<=0.62):
                child = mutationAgainstTime(child,x)
                pass


            elif(k<=1):
                child = mutationAgainstRoom(child,x)
                pass




    return child


def simpleMutation(Child = Classes.Chromosome()):

    randomNumbers = []
    #length = int(Child.geneList.__len__()/2)
    length = 3
    for x in range(length):

        randomNumbers.append(random.randint(0,Child.geneList.__len__()-1))


    for x in randomNumbers:

        z = np.random.random()

        if(z<0.4):
            #Mutation Day

            Child.geneList[x].Day = random.randint(0,4)

        elif(z<0.5):
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

        return Child


def mutationAgainstDay(child = Classes.Chromosome(),index=0):
    child.geneList[index].Day = random.randint(0, 4)
    return child

def mutationAgainstTime(child = Classes.Chromosome(),index=0):
    if (child.geneList[index].Type == 0):

        timeList = SetTime.set_timing_for_class()

        child.geneList[index].start_time = timeList[0]
        child.geneList[index].end_time = timeList[1]


    elif (child.geneList[index].Type == 1):

        timeList = SetTime.set_timing_for_lab()

        child.geneList[index].start_time = timeList[0]
        child.geneList[index].end_time = timeList[1]

    return child

def mutationAgainstRoom(child = Classes.Chromosome(),index=0):
    # Room

    if (child.geneList[index].Type == 0):

        child.geneList[index].Room = random.randint(2, 6)

        # lab
    elif (child.geneList[index].Type == 1):

        child.geneList[index].Room = random.randint(0, 1)

    return child