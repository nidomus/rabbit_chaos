from coelho import Coelho
import random as r
from movimentacao import Movimentacao
from time import sleep

class Jogo:

    def __init__(self) -> None:
           
        self.__mapa = []
        
        self.__coelhos = []
        decisoes = []

        for i in range(4):
            linha = []
            for j in range(4):
                linha.append(0)

            self.__mapa.append(linha)
    
    
    def instanciar_coelhos(self):

        cont = 0
        while cont != 5:

            i = r.randint(0,3)
            j = r.randint(0,3)

            if self.__mapa[i][j] == 0:

                self.__mapa[i][j] += 1


                c = Coelho(id=cont,coord=(i,j))

                self.__coelhos.append(c)

                cont += 1
                print(f'{c.get_coordenada()} -> {c.get_id()}')

        print()
        self.print_mapa()

    def iniciar_jogo(self):

        for coelho in self.__coelhos:
            
            while True:
                try: 
                    i, j = coelho.get_coordenada()
                    m=Movimentacao()

                    movimento = m.sortear_movimento()

                    aux_i, aux_j = movimento(i,j)

                    self.__mapa[aux_i][aux_j] +=1


                    self.__mapa[i][j] -=1

                    coelho.set_coordenada((aux_i,aux_j))

                    break
                
                except IndexError:
                    pass
        
        self.print_mapa()

    def print_mapa(self):

        for i in self.__mapa:
            print(i)
        

jogo = Jogo()

jogo.instanciar_coelhos()

while True:
    print()
    jogo.iniciar_jogo()
    sleep(2)