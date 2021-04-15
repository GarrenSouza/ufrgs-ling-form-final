import re

def parseAfd(file_path):
    file = open(file_path, encoding='utf8')
    afd = file.readline()
    afd = re.findall(r'(.*)=.*{(.*)},{(.*)},(.*),(.*),{(.*)}', afd)
    return afd[0]

parseAfd('input.txt')