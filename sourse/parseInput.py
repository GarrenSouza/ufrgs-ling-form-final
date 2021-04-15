import re
from pprint import pprint

def parseAfd(file_path):
    file = open(file_path, encoding='utf8')
    afd = re.findall(r'(.*)=.*{(.*)},{(.*)},(.*),(.*),{(.*)}', file.readline())[0]
    file.close()
    return {'name':afd[0], 'states':afd[1].split(','), 'alpha':afd[2].split(','), 'prog':afd[3], 'initial':afd[4], 'final':afd[5].split(',')}

