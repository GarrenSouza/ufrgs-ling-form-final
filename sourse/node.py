#Autores: Garrenlus de Souza, Lucas Rozado & Rodolfo Barbosa | 2021
#Representacao interna de um nodo do AFD

class AFDNode:
    def __init__(self, name, transitions=None, isFinal=False):
        self.name = name                #string
        self.transitions = transitions  #dictionary
        self.final = isFinal            #boolean

    def addTransition(self, input, nextState):
        self.transitions[input] = nextState
     
    def remove_transition(self, sym):
        self.transitions.pop(sym)

    def getNext(self, input):
        return self.transitions[input]

    def setAsFinal(self):
        self.final=True
    
    def getName(self):
        return self.name

    def isFinal(self):
        return self.final

    def getTransitions(self):
        return self.transitions

    def continue_avaliating(self, pair):
        return self.final == pair.final