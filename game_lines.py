from colorama import Fore, Style
from utils import clear, prints, slow_text_delay

def what_do():
    input('\nWhat do you do?\n')

def wrong_choice():
    '''Default message when a wrong choice in inputed by player'''
    input(Fore.RED + '\nINVALID CHOICE! Please enter a valid choice:\n' + Style.RESET_ALL, slow_text_delay)

def unavailable_feature():
    input('\nSorry, this feature isn\'t implemented yet :/ ...\n')
    clear()