import numpy as np
import random
import Classes



def RouletteWheelSelection(population = Classes.Population()):

    # chromosome , prob , CP  ]
    table =[]

    num = np.random.random(1)[0]





    # a = Classes.Chromosome()
    # b = Classes.Chromosome()
    # c = Classes.Chromosome()
    # d = Classes.Chromosome()
    # e = Classes.Chromosome()
    # f = Classes.Chromosome()
    # g = Classes.Chromosome()
    # h = Classes.Chromosome()
    # i = Classes.Chromosome()
    #
    #
    # a.fitness = -9
    # b.fitness = -5
    # c.fitness = -15
    # d.fitness = -22
    # e.fitness = -4
    # f.fitness = -12
    # g.fitness = -15
    # h.fitness = -9
    # i.fitness = -20

    #listChromosome = [a,b,c,d,e,f,g,h,i]
    #listChromosome = [-9,-5,-15,-22,-4,-12,-15,-9,-20]
    listChromosome = population.chromosomeList
    listChromosome.sort(key=lambda x: x.fitness, reverse=True)
    #listChromosome.sort(reverse=True)
    # print(listChromosome,"\n\n")

    sum = 0
    for x in listChromosome:
        sum = sum + x.fitness

    #print("\n\nSum = ",sum)
    prob = []

    for x in range(listChromosome.__len__()):
        prob.append( (((listChromosome[x].fitness/sum)*-1)))

    #print("\n\nProbability = ",prob)

    cp = []

    CpSum = 0
    for x in range(listChromosome.__len__()):
      CpSum = CpSum + prob[x]
      cp.append(CpSum * -1)

    #print("\n\nCummulative Probability = ",cp)

    # print(num,"\n\n")

    table.append(listChromosome)
    table.append(prob)
    table.append(cp)



    # start , end , difference
    ranges = [[],[],[]]
    st_Range = 0
    ed_Range = 0

    sum = 0
    for x in range(table[0].__len__()):

        if(x==0):
            st_Range=0
            ed_Range=table[2][0]
            ranges[0].append(st_Range)
            ranges[1].append(ed_Range)

        else:
            st_Range = table[2][x-1]
            ed_Range = table[2][x]
            ranges[0].append(st_Range)
            ranges[1].append(ed_Range)



    # print("Chr              Prob                         CP")
    # for x in range(table[0].__len__()):
    #     print(table[0][x],"       ",table[1][x],"       ",table[2][x],"                       ",ranges[0][x],"                             ",ranges[1][x])

    # print("\n\nDifferences\n\n\n")
    for x in range(ranges[0].__len__()):
        difference = (ranges[0][x] - ranges[1][x]) * -1
        ranges[2].append(difference)
        #print(difference)


    #plotting ranges

    FinalList = []
    for x in range(ranges[0].__len__()):
        maxmimumDifference = max(ranges[2])
        INDEX = ranges[2].index(maxmimumDifference)
        FinalList.append(Classes.RouletteChromosome(table[0][x],ranges[0][INDEX],ranges[1][INDEX]))
        ranges[0][INDEX] = 0
        ranges[1][INDEX] = 0
        ranges[2][INDEX] = 0



    # print("\n\nFinal Result\n\n")
    # for x in FinalList:
    #     print(x.chr,"       ",x.startRange,"        ",x.endingRange)
    #
    # return FinalList

    for x in FinalList:

        if(num>=x.startRange and num<x.endingRange):
            return x.chr