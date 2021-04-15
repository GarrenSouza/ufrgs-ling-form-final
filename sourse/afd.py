from sourse.parseInput import parseAfd

class Afd:
    def __init__(self, file_path):
        dict = parseAfd(file_path)
        self.name = dict['name']
        self.alpha = dict['alpha']
        self.initial_state = dict['initial']
        self.final_states = dict['final']
        self.states = dict['states']
        self.prog = dict['prog']
        self.nodes = None
    
    def __str__(self):
        return f'<{self.name}=(Q:{self.states}, E:{self.alpha}, {self.prog}, {self.initial_state}, F:{self.final_states})>'
    
    def __repr__(self):
        return self.__str__()

    def minimize(self):
        pass

    def makeTotal(self):    
        pass

