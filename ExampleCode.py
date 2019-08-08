'''

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
'''


# if(Day_matrix[2][x] == generalMatrix[1][index]):
#
#                 room_clash = Day_matrix[3][x]
#                 room_clash = room_clash + 1
#                 Day_matrix[3][x] = room_clash
#                 addEntry = False
#
#             if(Day_matrix[4][x][0] == generalMatrix[4][index]):
#
#                 Teacher_clash = Day_matrix[4][x][1]
#                 Teacher_clash = Teacher_clash + 1
#                 Day_matrix[4][x][1] = Teacher_clash
#                 addEntry = False
#
#             if(Day_matrix[5][x] == generalMatrix[5][index]):
#
#                 section_clash = Day_matrix[6][x][1]
#                 section_clash = section_clash + 1
#                 Day_matrix[6][x][1] = section_clash
#                 addEntry = False
