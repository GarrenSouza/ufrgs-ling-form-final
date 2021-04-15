import re

pprint()

# AFD stands for DFA which stands for Deterministic Finite Automaton

'''
    Given a path to an afd file returns a dictionary with:
        - the dfa's name:               name
        - the afd's states:             states
        - the afd's alphabet:           alpha
        - the afd's program function:   prog   
        - the afd's initial state:      initial
        - the afd's final states:       final
    Returns False if any errors occur

'''
def parseAfd(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            afd = re.findall(r'(.*)=.*{(.*)},{(.*)},(.*),(.*),{(.*)}', file.readline())[0]
        return {'name':afd[0], 'states':afd[1].split(','), 'alpha':afd[2].split(','), 'initial':afd[4], 'final':afd[5].split(',')}
    except:
        return False


'''
    Given a path to an afd file returns a dictionary with:
        - the departure state:                                                   dep_state
        - the arrival state:                                                     arr_state
        - the symbol used to go from the departure state to the arrival state:   symbol
    Returns False if any errors occur
        
'''

def parseNodes(file_path):
    try:
        with open(file_path, encoding='utf8') as file:
            nodes = file.read()
        nodes = re.findall(r'^\((.*),(.*)\)=(.*)', nodes, re.MULTILINE)
        return [{'dep_state':node[0], 'symbol':node[1], 'arr_state':node[2]} for node in nodes]
    except:
        return False



