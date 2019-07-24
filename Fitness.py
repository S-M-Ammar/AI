import Classes



def CalculateFitness(chrsm = Classes.Chromosome()):

    room_clash = 0
    teacher_clash = 0
    section_clash = 0
    friday_prayer_clash = 0

    general_matrix = generate_GeneralMatrix(chrsm)
    Days_Dictionary = set_elements_per_day(general_matrix)

    Monday_Matrix = Days_Dictionary[0]
    Tuesday_Matrix = Days_Dictionary[1]
    Wednesday_Matrix = Days_Dictionary[2]
    Thursday_Matrix = Days_Dictionary[3]
    Friday_Matrix = Days_Dictionary[4]

    for x in range(Monday_Matrix[0].__len__()):

        if(Monday_Matrix[3][x] > 1):
            room_clash = room_clash + (Monday_Matrix[3][x] - 1)

        if(Monday_Matrix[4][x][1] > 1):
            teacher_clash = teacher_clash + (Monday_Matrix[4][x][1] - 1)

        if(Monday_Matrix[6][x][1] > 1):
            section_clash = section_clash + (Monday_Matrix[6][x][1] - 1)


    for x in range(Tuesday_Matrix[0].__len__()):

        if (Tuesday_Matrix[3][x] > 1):
            room_clash = room_clash + (Tuesday_Matrix[3][x] - 1)

        if (Tuesday_Matrix[4][x][1] > 1):
            teacher_clash = teacher_clash + (Tuesday_Matrix[4][x][1] - 1)

        if (Tuesday_Matrix[6][x][1] > 1):
            section_clash = section_clash + (Tuesday_Matrix[6][x][1] - 1)

    for x in range(Wednesday_Matrix[0].__len__()):

        if (Wednesday_Matrix[3][x] > 1):
            room_clash = room_clash + (Wednesday_Matrix[3][x] - 1)

        if (Wednesday_Matrix[4][x][1] > 1):
            teacher_clash = teacher_clash + (Wednesday_Matrix[4][x][1] - 1)

        if (Wednesday_Matrix[6][x][1] > 1):
            section_clash = section_clash + (Wednesday_Matrix[6][x][1] - 1)

    for x in range(Thursday_Matrix[0].__len__()):

        if (Thursday_Matrix[3][x] > 1):
            room_clash = room_clash + (Thursday_Matrix[3][x] - 1)

        if (Thursday_Matrix[4][x][1] > 1):
            teacher_clash = teacher_clash + (Thursday_Matrix[4][x][1] - 1)

        if (Thursday_Matrix[6][x][1] > 1):
            section_clash = section_clash + (Thursday_Matrix[6][x][1] - 1)

    for x in range(Friday_Matrix[0].__len__()):

        if (Friday_Matrix[3][x] > 1):
            room_clash = room_clash + (Friday_Matrix[3][x] - 1)

        if (Friday_Matrix[4][x][1] > 1):
            teacher_clash = teacher_clash + (Friday_Matrix[4][x][1] - 1)

        if (Friday_Matrix[6][x][1] > 1):
            section_clash = section_clash + (Friday_Matrix[6][x][1] - 1)


    return [room_clash,teacher_clash,section_clash]


def generate_GeneralMatrix(chrms = Classes.Chromosome()):

    general_Matrix = [   []  ,  []  ,[]  , []  , [] , [] , [] ]
    # format = day  , room  , start - time  , end - time , teacher , batch , section

    i = 0
    for x in chrms.geneList:
        general_Matrix[0].append(x.Day)
        general_Matrix[1].append(x.Room)
        general_Matrix[2].append(x.start_time)
        general_Matrix[3].append(x.end_time)
        general_Matrix[4].append(x.Teacher)
        general_Matrix[5].append(x.Batch)
        general_Matrix[6].append(x.Section)

        i = i+1

    return general_Matrix


def set_elements_per_day(general_Matrix = []):

    Monday_matrix = [[], [], [], [] , [] , [] , []]
    Tuesday_matrix = [[], [], [], [] , [] , [] , []]
    Wednesday_matrix = [[], [], [], [] , [] , [] , []]
    Thursday_matrix = [[], [], [], [] , [] , [] , []]
    Friday_matrix = [[], [], [], [] , [] , [] , []]

    # day matrix format = start time , end time , room , room Occupation , Teacher Clash , batch , section_Clash

    for x in range(general_Matrix[0].__len__()):

        if(general_Matrix[0][x]==0): #Monday

           if(Monday_matrix[0].__len__()==0):
               Monday_matrix[0].append(general_Matrix[2][x]) # start time
               Monday_matrix[1].append(general_Matrix[3][x]) # end time
               Monday_matrix[2].append(general_Matrix[1][x]) # room
               Monday_matrix[3].append(1)                    # room occupation
               Monday_matrix[4].append([general_Matrix[4][x],1]) # teacher code
               Monday_matrix[5].append(general_Matrix[5][x]) # batch number
               Monday_matrix[6].append([general_Matrix[6][x],1]) # section code



           else:

               Monday_matrix = entries_check(Monday_matrix , general_Matrix  , x )


        elif(general_Matrix[0][x]==1): #tuesday

            if (Tuesday_matrix[0].__len__() == 0):
                Tuesday_matrix[0].append(general_Matrix[2][x])  # start time
                Tuesday_matrix[1].append(general_Matrix[3][x])  # end time
                Tuesday_matrix[2].append(general_Matrix[1][x])  # room
                Tuesday_matrix[3].append(1)  # room occupation
                Tuesday_matrix[4].append([general_Matrix[4][x], 1])  # teacher code
                Tuesday_matrix[5].append(general_Matrix[5][x])  # batch number
                Tuesday_matrix[6].append([general_Matrix[6][x], 1])  # section code

            else:

                Tuesday_matrix = entries_check(Tuesday_matrix, general_Matrix, x)

        elif (general_Matrix[0][x] == 2): #wednesday

            if (Wednesday_matrix[0].__len__() == 0):
                Wednesday_matrix[0].append(general_Matrix[2][x])  # start time
                Wednesday_matrix[1].append(general_Matrix[3][x])  # end time
                Wednesday_matrix[2].append(general_Matrix[1][x])  # room
                Wednesday_matrix[3].append(1)  # room occupation
                Wednesday_matrix[4].append([general_Matrix[4][x], 1])  # teacher code
                Wednesday_matrix[5].append(general_Matrix[5][x])  # batch number
                Wednesday_matrix[6].append([general_Matrix[6][x], 1])  # section code


            else:

                Wednesday_matrix = entries_check(Wednesday_matrix, general_Matrix, x)

        elif (general_Matrix[0][x] == 3): # thursday

            if (Thursday_matrix[0].__len__() == 0):
                Thursday_matrix[0].append(general_Matrix[2][x])  # start time
                Thursday_matrix[1].append(general_Matrix[3][x])  # end time
                Thursday_matrix[2].append(general_Matrix[1][x])  # room
                Thursday_matrix[3].append(1)  # room occupation
                Thursday_matrix[4].append([general_Matrix[4][x], 1])  # teacher code
                Thursday_matrix[5].append(general_Matrix[5][x])  # batch number
                Thursday_matrix[6].append([general_Matrix[6][x], 1])  # section code

            else:

                Thursday_matrix = entries_check(Thursday_matrix, general_Matrix, x)

        elif (general_Matrix[0][x] == 4):  # friday

            if (Friday_matrix[0].__len__() == 0):
                Friday_matrix[0].append(general_Matrix[2][x])  # start time
                Friday_matrix[1].append(general_Matrix[3][x])  # end time
                Friday_matrix[2].append(general_Matrix[1][x])  # room
                Friday_matrix[3].append(1)  # room occupation
                Friday_matrix[4].append([general_Matrix[4][x], 1])  # teacher code
                Friday_matrix[5].append(general_Matrix[5][x])  # batch number
                Friday_matrix[6].append([general_Matrix[6][x], 1])  # section code

            else:

                Friday_matrix = entries_check(Friday_matrix, general_Matrix, x)

    #creating dictionary

    Days_Dictionary = {0:Monday_matrix,1:Tuesday_matrix,2:Wednesday_matrix,3:Thursday_matrix,4:Friday_matrix}

    return Days_Dictionary



def entries_check(Day_matrix = [] , generalMatrix = []  , index = 0):

    # day matrix format = start time , end time , room , room Occupation , Teacher Clash , batch number , section Clash

    # general matrix format = day  , room  , start - time  , end - time , teacher , batch , section

    #check Room Clash
    #check Teacher Clash
    #check Section Clash

    addEntry = True



    for x in range(len(Day_matrix[0])):

        time_is_equal = False
        lie_in_between = False

        start_time = Day_matrix[0][x]
        end_time = Day_matrix[1][x]

        generalMatrix_startTime = generalMatrix[2][index]
        generalMatrix_endTime = generalMatrix[3][index]

        if(start_time[0]==generalMatrix_startTime[0] and start_time[1]==generalMatrix_startTime[1] and end_time[0]==generalMatrix_endTime[0] and end_time[1]==generalMatrix_endTime[1]):

            time_is_equal = True

            if(Day_matrix[2][x] == generalMatrix[1][index]):

                room_clash = Day_matrix[3][x]
                room_clash = room_clash + 1
                Day_matrix[3][x] = room_clash
                addEntry = False

            if(Day_matrix[4][x][0] == generalMatrix[4][index]):

                Teacher_clash = Day_matrix[4][x][1]
                Teacher_clash = Teacher_clash + 1
                Day_matrix[4][x][1] = Teacher_clash
                addEntry = False

            if(Day_matrix[5][x] == generalMatrix[5][index]):

                section_clash = Day_matrix[6][x][1]
                section_clash = section_clash + 1
                Day_matrix[6][x][1] = section_clash
                addEntry = False




        #check if new entry start time or end time lies in between any existing entry

        if(generalMatrix_startTime[0]>=start_time[0] and generalMatrix_startTime[1] >= start_time[1] and generalMatrix_startTime[0] <=end_time[0] and generalMatrix_startTime[1]<=end_time[1] and time_is_equal==False ):

            lie_in_between = True

            if (Day_matrix[2][x] == generalMatrix[1][index]):
                room_clash = Day_matrix[3][x]
                room_clash = room_clash + 1
                Day_matrix[3][x] = room_clash
                addEntry = False

            if (Day_matrix[4][x][0] == generalMatrix[4][index]):
                Teacher_clash = Day_matrix[4][x][1]
                Teacher_clash = Teacher_clash + 1
                Day_matrix[4][x][1] = Teacher_clash
                addEntry = False

            if (Day_matrix[5][x] == generalMatrix[5][index]):
                section_clash = Day_matrix[6][x][1]
                section_clash = section_clash + 1
                Day_matrix[6][x][1] = section_clash
                addEntry = False

        elif(generalMatrix_endTime[0]>=start_time[0] and generalMatrix_endTime[1]>=start_time[1] and generalMatrix_endTime[0]<=end_time[0] and generalMatrix_endTime[1]<=end_time[1]and time_is_equal==False):

            lie_in_between = True

            if (Day_matrix[2][x] == generalMatrix[1][index]):
                room_clash = Day_matrix[3][x]
                room_clash = room_clash + 1
                Day_matrix[3][x] = room_clash
                addEntry = False

            if (Day_matrix[4][x][0] == generalMatrix[4][index]):
                Teacher_clash = Day_matrix[4][x][1]
                Teacher_clash = Teacher_clash + 1
                Day_matrix[4][x][1] = Teacher_clash
                addEntry = False

            if (Day_matrix[5][x] == generalMatrix[5][index]):
                section_clash = Day_matrix[6][x][1]
                section_clash = section_clash + 1
                Day_matrix[6][x][1] = section_clash
                addEntry = False

        #check whether any existing entry lies in between interval of new entry


        if(lie_in_between==False and time_is_equal==False):

            if(start_time[0]>=generalMatrix_startTime[0] and start_time[1]>=generalMatrix_startTime[1] and end_time[0]<=generalMatrix_endTime[0] and end_time[1]<=generalMatrix_endTime[1]):

                if (Day_matrix[2][x] == generalMatrix[1][index]):
                    room_clash = Day_matrix[3][x]
                    room_clash = room_clash + 1
                    Day_matrix[3][x] = room_clash
                    addEntry = False

                if (Day_matrix[4][x][0] == generalMatrix[4][index]):
                    Teacher_clash = Day_matrix[4][x][1]
                    Teacher_clash = Teacher_clash + 1
                    Day_matrix[4][x][1] = Teacher_clash
                    addEntry = False

                if (Day_matrix[5][x] == generalMatrix[5][index]):
                    section_clash = Day_matrix[6][x][1]
                    section_clash = section_clash + 1
                    Day_matrix[6][x][1] = section_clash
                    addEntry = False







    if(addEntry):
        Day_matrix[0].append(generalMatrix[2][index])  # start time
        Day_matrix[1].append(generalMatrix[3][index])  # end time
        Day_matrix[2].append(generalMatrix[1][index])  # room
        Day_matrix[3].append(1)
        Day_matrix[4].append([generalMatrix[4][index], 1])  # teacher code
        Day_matrix[5].append(generalMatrix[5][index]) # batch number
        Day_matrix[6].append([generalMatrix[6][index],1]) # section code


    return Day_matrix


def printGeneralMatrix(matrix=[]):

    print("DAY","   ","ROOM","  ","START TIME","    ","END TIME","      ","Teacher","\n")

    for x in range(len(matrix[0])):

        print(matrix[0][x],"        ",matrix[1][x],"    ",matrix[2][x],"      ",matrix[3][x],"          ",matrix[4][x],"\n")


