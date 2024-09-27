from utils import load_dialogs, prints, prints_plus, dprint
from game_lines import what_do, wrong_choice

def init_dialogs():
    '''import all the dialogs used in this area'''
    global dialogs
    dialogs = {}
    load_dialogs('dialogs/story_01.json')

def wake_up():
    prints_plus('......', 0.5)
    dprint('wake_up_010')
    dprint('wake_up_020')
    dprint('wake_up_030')
    dprint('wake_up_040')
    what_do()
    