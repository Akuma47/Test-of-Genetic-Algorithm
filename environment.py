
from numpy import random
from numpy.random.mtrand import rand, randint
import random
import numpy as np


target = [1,2,3,4]

def fitness(populacao):

    points = 0
    for h in range(len(target)):
            
        for j in range(len(populacao)):
            if populacao[j] == target[h]:
                points+=1
            

    points = points / len(target)

    return points


def selection(populacao):
    selecionados = []

    for i in range(len(populacao)):
        n = fitness(populacao[i]) * 100

        x = 0
        while(x<n):
            selecionados.append(populacao[i])
            x+=1
    return selecionados

def crossover(selecionados):

    a = randint(0,len(selecionados))
    b = randint(0,len(selecionados))

    parentA = selecionados[a]
    parentB = selecionados[b]


    child = []
    n = int(int(len(parentA)) /2)
    for i in range(n):
        child.append(parentA[i])

    for i in range(n):
        child.append(parentB[n+i])


    return child




def mutation(child,pop): 

    MutationRate = 0.1
    r = random.uniform(0,1)

    rand = randint(0,len(child))

    if r < MutationRate:
        print("Child: ",child)

        print('Mutação ocorrida')
        child[rand] = np.random.randint(0,len(pop))

    print('Melhor individuo: ', child)
    return child




































