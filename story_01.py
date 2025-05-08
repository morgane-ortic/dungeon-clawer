from utils import load_dialogs, prints, prints_plus, printd, print_choice, print_line
from character import NPC
from game_lines import what_do, wrong_choice


class LevelStory01:

    def __init__(self, pc):
        # assign pc to class attribute
        self.pc = pc
        # Create all npcs for the level
        self.create_npcs()
        # Initialize all dialogs for the next area
        self.init_dialogs()

    def create_npcs(self):
        self.npc_bandit_1 = NPC('npcs.json', 'thug')
        self.npc_bandit_2 = NPC('npcs.json', 'thug')
        self.npc_bandit_3 = NPC('npcs.json', 'thug')
        self.npc_bandit_4 = NPC('npcs.json', 'thug')

    def init_dialogs(self):
        '''import all the dialogs used in this area'''
        self.dialogs = {}
        load_dialogs('dialogs/story_01.json')

    def wake_up(self):
        prints_plus('...', 0.5)
        printd('wake_up_010')
        printd('wake_up_020')
        roll_per_10 = self.npc_bandit_1.roll('stealth')
        if roll_per_10 >= self.pc.pp:
            printd('npc_stealth_10_success')
        else:
            printd('npc_stealth_10_fail')

        what_do()
        print_choice('choice_back_to_bed_10')
        print_choice('choice_back_to_bed_20')
        while True:
            choice_back_to_bed = input('\n')
            print_line()
            if choice_back_to_bed == '1':
                printd('choice_back_to_bed_yes')
                break
            elif choice_back_to_bed == '2':
                printd('choice_back_to_bed_no')
                break
        
        print('To be continued...')

    def combat_1():
        #this will be a new chapter inside the level
        pass