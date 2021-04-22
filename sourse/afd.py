
# AFD stands for DFA which stands for Deterministic Finite Automaton

from parseInput import parseAfd, parseNodes
from node import AFDNode

class AFD:
    def __init__(self, file_path):
        dict = parseAfd(file_path)
        if not dict:
            print(f'No such file or directory: \'{file_path}\'')
            return 
        self.name = dict['name']
        self.alpha = dict['alpha']
        self.initial_state = dict['initial']
        self.final_states = dict['final']
        self.states = dict['states']
        self.nodes = self.addNodesFile(file_path)
    
    def __str__(self):
        return f'<{self.name}=(Q:{self.states}, E:{self.alpha}, {self.initial_state}, F:{self.final_states})>'
    
    def __repr__(self):
        return self.__str__()
    
    def addNodesFile(self, file_path):
        parsed_nodes = parseNodes(file_path, self.states)
        nodes = list()
        # Creates a list of nodes with a 'Label' name
        for parsed_node in parsed_nodes:
            node = AFDNode(parsed_node, dict(), parsed_node in self.final_states)
            for dict_element in parsed_nodes[parsed_node]:
                node.addTransition(dict_element['symbol'], dict_element['state'])
            nodes.append(node)
        # Changes the 'Label' for the node now it's created
        for searched_node in nodes:
            for node in nodes:
                for symbol, state in node.transitions.items():
                    if searched_node.name == state:
                        node.transitions[symbol] = searched_node
        return nodes
   
    def makeTotal(self):
        i = 0
        # Checks the transitions of each node
        for node in self.nodes:
            for sym in self.alpha:
                # if there isn't a transition with the current symbol
                # creates a trap state 
                if not sym in node.transitions:
                    trap_node = AFDNode(f'Trap{i}', dict())
                    # For each symbol the trap states references itself
                    for _sym in self.alpha:
                        trap_node.addTransition(_sym, trap_node)
                    # Adds a transition with the missing symbol from current
                    # node to the trap state of index i
                    node.addTransition(sym, trap_node)
                    self.nodes.append(trap_node)
                    i += 1     

    def minimize(self):
        pass

    def removeUnreachableStates(self):
        reachable_nodes = {}
        nodes = {}
        for node in self.nodes:
            nodes[node.getName()] = node
        processing_queue = []
        processing_queue.append(nodes[self.initial_state])
        while len(processing_queue) > 0:
            node = processing_queue.pop(0)
            if reachable_nodes.get(node.getName()) == None:
                reachable_nodes[node.getName()] = node
                transitions = node.getTransitions()
                for tnode in transitions.values():
                    processing_queue.append(tnode)
        self.nodes = reachable_nodes
    
    def processWord(self, word, verbose=False):
        path = []
        symbol_position = 0
        nextState = self.nodes[self.initial_state]
        while nextState != None and symbol_position < len(word):
            path.append(nextState.getName())
            nextState = nextState.transitions[word[symbol_position]]
            symbol_position += 1
        if not nextState:
            if verbose:
                print("Word rejected (transition undefined)")
            return False
        else:
            if nextState.isFinal():
                path.append(nextState.getName())
                if verbose:
                    print("Word accepted")
                    print(path[0], end='')
                    for i in range(1,len(path)):
                        print(" -> "+path[i], end='')
                return True
            else:
                if verbose:
                    print("Word rejected (ending state is not final)")
                return False

afd = AFD('input.txt')