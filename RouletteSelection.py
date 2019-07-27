import numpy as np

listChromosome = [-9,-5,-15,-22,-4,-12,-15,-9,-20]

sum = 0
for x in listChromosome:
    sum = sum + x

print(sum)

prob = []

for x in range(listChromosome.__len__()):
    prob.append( round(((listChromosome[x]/sum)*-1),2))

print(prob)

cp = []

CpSum = 0
for x in range(listChromosome.__len__()):
  CpSum = CpSum + prob[x]
  cp.append(round(CpSum,2))

print(cp)

num = np.random.random()
print(num)

listChromosome.sort(reverse=True)
print(listChromosome)