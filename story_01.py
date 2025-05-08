from utils import load_dialogs, prints, prints_plus, print_dialog as printd
from character import NPC
from game_lines import what_do, wrong_choice

def create_npcs():
    global bandit_1, bandit_2, bandit_3, bandit_4
    bandit_1 = NPC('npcs.json', 'thug')
    bandit_2 = NPC('npcs.json', 'thug')
    bandit_3 = NPC('npcs.json', 'thug')
    bandit_4 = NPC('npcs.json', 'thug')

def init_dialogs():
    '''import all the dialogs used in this area'''
    global dialogs
    dialogs = {}
    load_dialogs('dialogs/story_01.json')

def wake_up(pc):
    prints_plus('...', 0.5)
    printd('wake_up_010')
    printd('wake_up_020')
    roll_per_10 = bandit_1.roll('stealth')
    if roll_per_10 >= pc.pp:
        printd('npc_stealth_10_success')
    else:
        printd('npc_stealth_10_fail')

    what_do()
    printd('choice_back_to_bed_10')
    printd('choice_back_to_bed_20')
    while True:
        choice_back_to_bed = input()
        if choice_back_to_bed == '1':
            printd('choice_back_to_bed_yes')
            break
        elif choice_back_to_bed == '2':
            printd('choice_back_to_bed_no')
            break
    
    print('To be continued...')