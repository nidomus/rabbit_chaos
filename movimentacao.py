import random as r

class Movimentacao:

    def __init__(self) -> None:

        self.__decisoes=[]

        self.__decisoes.append(self.move_cima)
        self.__decisoes.append(self.move_baixo)
        self.__decisoes.append(self.move_esquerda)
        self.__decisoes.append(self.move_direita) 
        

    def sortear_movimento(self):
        return self.__decisoes[r.randint(0,3)]
    
    def move_cima(self,i,j):
        if(i-1 <0):
            raise IndexError

        return i-1,j

    def move_baixo(self,i,j):
        return i+1,j

    def move_esquerda(self,i,j):
        if(j-1 <0):
            raise IndexError
        
        return i,j-1

    def move_direita(self,i,j):

        return i,j+1


