#Autores: Garrenlus de Souza, Lucas Rozado & Rodolfo Barbosa | 2021
#Representacao interna dos pares utilizados na etapa de teste de equivalencia do processo de minimizacao de AFD

class Pair:
    def __init__(self, name, l_node, r_node):
        self.name = name
        self.dependants_dict = dict()
        self.equivalent = True
        self.l_node = l_node
        self.r_node = r_node

    def __str__(self):
        return f'<{self.name}, {self.dependants_dict}, {self.equivalent}>'
    
    def __repr__(self):
        return self.__str__()
    
    # insere um par no dicionário de dependentes
    def insert_dependant(self, pair):
        self.dependants_dict[pair.name] = pair
    
    # Invalida um par e suas respectivas dependencias
    def invalidate(self):
        if self.equivalent:
            self.equivalent = False
            for pair in self.dependants_dict.values():
                pair.invalidate()
