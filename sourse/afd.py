
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



afd = AFD('input.txt')