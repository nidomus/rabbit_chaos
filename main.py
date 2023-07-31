import random as r
import time as t

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(0)

    matriz.append(linha)


c1_i = r.randint(0,4)
c1_j = r.randint(0,4)

matriz[c1_i][c1_j] +=1

c2_i = r.randint(0,4)
c2_j = r.randint(0,4)

matriz[c2_i][c2_j] +=1

decisoes = []

def move_cima(i,j):
    if(i-1 <0):
        
        raise IndexError

    return i-1,j

def move_baixo(i,j):
    return i+1,j

def move_esquerda(i,j):
    if(j-1 <0):
        raise IndexError
    
    return i,j-1

def move_direita(i,j):

    return i,j+1


decisoes.append(move_cima)
decisoes.append(move_baixo)
decisoes.append(move_esquerda)
decisoes.append(move_direita)


for linha in matriz:
    print(linha)


while True:


    while True:
        try:

            new_i, new_j = decisoes[r.randint(0,3)](c1_i,c1_j)

            
            matriz[new_i][new_j] += 1

            matriz[c1_i][c1_j] -= 1

            c1_i,c1_j = new_i, new_j

            break

        except IndexError:
            pass
        
    while True:
        
        try:

            new_i, new_j = decisoes[r.randint(0,3)](c2_i,c2_j)

            
            matriz[new_i][new_j] += 1

            matriz[c2_i][c2_j] -= 1

            c2_i,c2_j = new_i, new_j

            break

        except IndexError:
            pass
        
    for linha in matriz:
            print(linha)
    t.sleep(1)        