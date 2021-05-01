
# AFD stands for DFA which stands for Deterministic Finite Automaton

from parseInput import parseAfd, parseNodes
from node import AFDNode
from pair import Pair

class AFD:
    def __init__(self, file_path):
        parsed_file = parseAfd(file_path)
        if not parsed_file:
            print(f'No such file or directory: \'{file_path}\'')
            return 
        self.name = parsed_file['name']
        self.alpha = parsed_file['alpha']
        self.initial_state = parsed_file['initial']
        self.final_states = parsed_file['final']
        self.states = parsed_file['states']
        self.nodes = self.addNodesFile(file_path)
    
    def __str__(self):
        return f'<{self.name}=(Q:{self.states}, E:{self.alpha}, {self.initial_state}, F:{self.final_states})>'
    
    def __repr__(self):
        return self.__str__()
    
    def addNodesFile(self, file_path):
        parsed_nodes = parseNodes(file_path, self.states)
        nodes = dict()
        # Creates a list of nodes with a 'Label' name
        for parsed_node in parsed_nodes:
            node = AFDNode(parsed_node, dict(), parsed_node in self.final_states)
            for dict_element in parsed_nodes[parsed_node]:
                node.addTransition(dict_element['symbol'], dict_element['state'])
            nodes[node.name] = node
        # Changes the 'Label' for the node now it's created
        for searched_node in nodes.values():
            for node in nodes.values():
                for symbol, state in node.transitions.items():
                    if searched_node.name == state:
                        node.transitions[symbol] = searched_node
        return nodes
   
    def makeTotal(self):
        # Create Trap State
        trap_node = AFDNode('Trap', dict())
        needs_trap = False
        # Checks the transitions of each node
        for node in self.nodes.values():
            for sym in self.alpha:
                # if there isn't a transition with the current symbol
                # creates a trap state 
                if not sym in node.transitions:
                    needs_trap = True
                    # Adds a transition with the missing symbol from current
                    # node to the trap state
                    node.addTransition(sym, trap_node)
        if needs_trap:
            for sym in self.alpha:
                trap_node.addTransition(sym, trap_node)
            self.nodes[trap_node.name] = trap_node
            self.states.append(trap_node.name)

    def removeUnreachableStates(self):
        reachable_nodes = {}
        processing_queue = []
        processing_queue.append(self.nodes[self.initial_state])
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

    def remove_node(self, name):
        self.nodes.pop(name)
        for index, state in enumerate(self.states):
            if name == state:
                self.states.pop(index)
                return


    def minimize(self):
        self.removeUnreachableStates()
        self.makeTotal()
        # Teste de equivalencia de estados
        pairs_dict = dict()
        node_list = list(self.nodes.values())
        ## Cria um dicionário de dependencias
        for pivot, value in enumerate(node_list):
            for cursor in node_list[pivot + 1:]:
                name = value.name + cursor.name
                pairs_dict[name] = Pair(name, value, cursor)
        ##
        for pair in pairs_dict.values():
            if pair.l_node.continue_avaliating(pair.r_node):
                ## Itera sobre o alfabeto
                for sym in self.alpha:
                    ## Próximos estados iguais
                    if pair.l_node.getNext(sym).getName() == pair.r_node.getNext(sym).getName():
                        continue
                    key1 = pair.l_node.getNext(sym).getName() + pair.r_node.getNext(sym).getName()
                    key2 = pair.r_node.getNext(sym).getName() + pair.l_node.getNext(sym).getName()
                    key = key1 if pairs_dict.get(key1) != None else key2
                    ## Adiciona o par na lista de dependencias relativa as transições
                    if pairs_dict[key].equivalent:
                        pairs_dict[key].insert_dependant(pair)
                    ## Invalida par
                    else:
                        pair.invalidate()
            else:
                pair.invalidate()
        # Unificação de estados equivalentes
        for pair in pairs_dict.values():
            if pair.equivalent:
                # Percorre nodo
                for node in self.nodes.values(): 
                    # Percorre as transições do Nodo
                    for key, value in node.transitions.items():
                        if value == pair.r_node:
                            node.transitions[key] = pair.l_node
                # Deleta duplicata
                self.remove_node(pair.r_node.name)
        # Exclusão de estados inuteis
        ## Procura por estdos inuteis
        useless_states = list()
        for node in self.nodes.values():
            parsing_queue = [node]
            tracking_dict = dict()
            reaches_final = False
            # Procura por estados finais a partir do Nodo atual
            while len(parsing_queue):
                _node = parsing_queue.pop(0)
                if _node.final:
                    reaches_final = True
                    break
                for transition in _node.transitions.values():
                    if not transition.name in tracking_dict:
                        tracking_dict[transition.name] = transition.name 
                        parsing_queue.append(transition)

            if not reaches_final:
                useless_states.append(node)
        # Remove estados inuteis
        print(useless_states[0].name)



        # Construção do AFD minimizado

                

            


afd = AFD('input.txt')