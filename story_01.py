from utils import load_dialogs, prints, prints_plus, dprint

def init_dialogs():
    '''import all the dialogs used in this area'''
    load_dialogs('dialogs/story_01.json')
    load_dialogs('dialogs/game_lines.json')

def wake_up():
    prints_plus('......', 0.5)
    dprint('wake_up_10')
    dprint('wake_up_20')
    dprint('wake_up_30')
    dprint('what_do')