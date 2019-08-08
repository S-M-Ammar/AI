import Classes
import CodeList
import GenerateTime
import SetTime
import random
import Fitness


def GenerateChromosome(Time_List):
    # create a chromosome consisting of multiple genes

    chromosome1 = Classes.Chromosome()

    CodeList.Time = Time_List

    for x in CodeList.course_database:

        timeList = []
        del timeList

        if (CodeList.course_database[x][2] == 0):

            timeList = SetTime.set_timing_for_class()

            chromosome1.geneList.append(
                Classes.ChromosomeGene(CodeList.course_database[x][0], CodeList.course_database[x][1],
                                       CodeList.course_database[x][3], CodeList.course_database[x][2],
                                       CodeList.course_database[x][4], random.randint(2, 7), timeList[0], timeList[1],
                                       random.randint(0, 4)))








        elif (CodeList.course_database[x][2] == 1):

            timeList = SetTime.set_timing_for_lab()
            chromosome1.geneList.append(
                Classes.ChromosomeGene(CodeList.course_database[x][0], CodeList.course_database[x][1],
                                       CodeList.course_database[x][3], CodeList.course_database[x][2],
                                       CodeList.course_database[x][4], random.randint(0, 1), timeList[0], timeList[1],
                                       random.randint(0, 4)))




    Clash_List = Fitness.CalculateFitness(chromosome1)
    chromosome1.fitness = (Clash_List[0] + Clash_List[1] + Clash_List[2])  * -1
    return chromosome1

