import numpy as np
from organism import *
from environment import *



pop = 10
gen = 4
newChild = 0

best = []

run = True
count = 0
while(run):
    print("=== Epoca: ",count)
    population = populacao(pop,gen,newChild)

    print(' - Selecao')
    selecionados = selection(population)

    print(' - Crossover')
    child = crossover(selecionados)
    
    print(' - Mutação')
    newChild = mutation(child,population)
    newChild = [newChild]
    
    if newChild[0] == target:
        print('=== END ==')
        print(count)
        print(newChild[0],target)
        best.append(newChild[0])
        run = False
    print('')
    count+=1

print('')
print(' === Fim ===')
print('')


print(best)





















