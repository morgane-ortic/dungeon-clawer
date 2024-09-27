from utils import load_dialogs, prints, prints_plus, print_dialog as printd
from game_lines import what_do, wrong_choice

def init_dialogs():
    '''import all the dialogs used in this area'''
    global dialogs
    dialogs = {}
    load_dialogs('dialogs/story_01.json')

def wake_up():
    prints_plus('......', 0.5)
    printd('wake_up_010')
    printd('wake_up_020')
    printd('wake_up_030')
    printd('wake_up_040')
    what_do()
    