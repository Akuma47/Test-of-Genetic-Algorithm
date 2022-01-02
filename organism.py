import numpy as np
from numpy.random.mtrand import randint



def cromo(tamGen):

    cromossomo = []
    for i in range(tamGen):
        rand = randint(0,10)
        cromossomo.append(rand)

    return cromossomo




def populacao(tamPop,tamGen,newchild):

    if newchild == 0:
        print('Criando nova populacao')
        populacao = []

        print('Criando Genes')
        for i in range(tamPop):
            populacao.append(cromo(tamGen))

        return populacao

    else:
        for i in range(tamPop - 1):
            newchild.append(cromo(tamGen))

        print("New: ", newchild)
        return newchild




















