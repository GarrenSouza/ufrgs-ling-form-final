class AFDNode:
    def __init__(self, name, transitions=None, isFinal=False):
        self.__name = name                #string
        self.__transitions = transitions  #dictionary
        self.__final = isFinal            #boolean

    def addTransition(self, input, nextState):
        self.__transitions[input] = nextState

    def __str__(self):
        info = f'<(label:{self.__name}, '
        if(len(self.__transitions.values()) > 0):
            for transition in self.__transitions.items()[:-1]:
                info += "[" + transition.key() + " -> " + transition.value().getName() + "], "
            info += "[" + transition.key() + " -> " + self.__transitions.items()[-1].getName() + "]"
        info += ")>"
        return info

    def __repr__(self):
        return self.__str__()

    def getNext(self, input):
        return self.__transitions.get(input) # me enganei, foi sobre o get que comentei no Discord

    def setAsFinal(self):
        self.__final=True
    
    def getName(self):
        return self.__name

    def isFinal(self):
        return self.__final

    def getTransitions(self):
        return self.__transitions
