
class Pair:
    def __init__(self, name):
        self.name = name
        self.dependants_dict = dict()
        self.equivalent = True
    
    # insere um par no dicionário de dependentes
    def insert_dependant(self, pair):
        self.dependants_dict[pair.name] = pair
    
    # Invalida um par e suas respectivas dependencias
    def invalidate(self):
        if self.equivalent:
            self.equivalent = False
            for pair in self.dependants_dict.values():
                pair.invalidate()
