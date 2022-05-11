
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for i in range(90, 120):
    cor = '\033[' + str(i) + 'm'
    print(f'{i} - {cor} TEXTO {bcolors.ENDC}')
#print(f'{bcolors.OKGREEN} COR {bcolors.ENDC}')
