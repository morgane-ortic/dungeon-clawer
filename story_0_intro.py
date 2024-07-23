from colorama import Fore, Style

import time

from utils import prints, slow_text_delay

# Most text is printed in typewriting style using prints, defined in utils.py

def story_intro():
    '''Print the story's introduction'''
    prints('Ortic productions presents\n', slow_text_delay)
    prints(Fore.RED + '          KARLACH' + Style.RESET_ALL, slow_text_delay)
    time.sleep(0.5)
    prints('            in\n')
    time.sleep(1)
    prints(Fore.RED + 'D U N G E O N   C L A W E R\n' + Style.RESET_ALL, slow_text_delay)
    time.sleep(0.8)
    input('Press Enter to start the game...')
    print()