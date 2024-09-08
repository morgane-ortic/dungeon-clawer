from utils import load_dialogs, prints, prints_plus, dprint

def init_dialogs():
    '''import all the dialogs used in this area'''
    load_dialogs('dialogs/story_01_test.json')

def wake_up():
    prints_plus('......', 0.5)
    dprint('narrator', 'wake_up_10')
    dprint('narrator', 'wake_up_20')
    dprint('narrator', 'wake_up_30')