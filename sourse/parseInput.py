import re

#Autores: Garrenlus de Souza, Lucas Rozado & Rodolfo Barbosa | 2021

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

def parseNodes(file_path, states):
    try:
        with open(file_path, encoding='utf8') as file:
            nodes = re.findall(r'^\((.*),(.*)\)=(.*)', file.read(), re.MULTILINE)
        nodes = [{'dep_state':node[0], 'symbol':node[1], 'arr_state':node[2]} for node in nodes]
        nodesDict = dict()
        for state in states:
            nodesDict[state] = list()
        for node in nodes:
            nodesDict[node['dep_state']].append({'state':node['arr_state'], 'symbol':node['symbol']})
        return nodesDict
    except:
        return False

def parse_pairs(file_path):
    try:
        with open(file_path, encoding='utf8') as file:
            return re.findall(r'(.*),(.*)', file.read(), re.MULTILINE) 
    except:
        return None
