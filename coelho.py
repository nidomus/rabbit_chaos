class Coelho():

    def __init__(self, coord, id) -> None:
        
        self.__id = id
        self.__tempo_vida = 10
        self.__coordenada = coord
        
        #self.__eh_filho = False
        #self.__fase = False


    def get_coordenada(self):

        return self.__coordenada
    
    def get_id(self):
        return self.__id
    
    def set_coordenada(self, coord):
        self.__coordenada = coord