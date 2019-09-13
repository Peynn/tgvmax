BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
GRAY = '\033[90m'
RESET = '\033[0m'

def cprint(color, *text):
    text = ' '.join([str(x) for x in text])

    if color is None:
        print(text)
    else:
        print(color + text + RESET)
