class AFDNode:
    def __init__(self, name, transitions=None, isFinal=False):
        self.name = name                #string
        self.transitions = transitions  #dictionary
        self.final = isFinal            #boolean

    def addTransition(self, input, nextState):
        self.transitions[input] = nextState
    
    '''
    def __str__(self):
        info = f'<(label:{self.name}, '
        if(len(self.transitions.values()) > 0):
            for transition in self.transitions.items()[:-1]:
                info += "[" + transition.key() + " -> " + transition.value().getName() + "], "
            info += "[" + transition.key() + " -> " + self.transitions.items()[-1].getName() + "]"
        info += ")>"
        return info

    def __repr__(self):
        return self.__str__()
    '''  

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