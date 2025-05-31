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
        roll_stealth_npc_10 = self.npc_bandit_1.roll('stealth')
        # Here the skill dice roll is checked against the pc's passive perception
        if roll_stealth_npc_10 >= self.pc.pp:
            printd('npc_stealth_10_success')
            self.npc_stealth_success()
        else:
            printd('npc_stealth_10_fail')
            self.npc_stealth_fail()

    def npc_stealth_success(self):
        what_do()
        print_choice('choice_back_to_bed_10', 'choice_back_to_bed_20')
        while True:
            choice_back_to_bed = input('\n')
            print_line()
            if choice_back_to_bed == '1':
                printd('choice_back_to_bed_yes')
                break
            elif choice_back_to_bed == '2':
                printd('choice_back_to_bed_no')
                break

    def npc_stealth_fail(self):
        what_do()
        print_choice('choice_check_window_10', 'choice_check_window_20')
        while True:
            choice_check_window = input('\n')
            print_line()
            if choice_check_window == '1':
                self.check_window()
            elif choice_check_window == '2':
                printd('choice_back_to_bed_yes')
                break

    def check_window(self):
        roll_per_pc_10 = self.pc.roll('perception')
        # Here the skill dice roll is checked against the fixed Challenge Rating for this test
        if roll_per_pc_10 >= 13:
            printd('pc_per_10_success')
            self.pc_per_success()
        else:
            printd('pc_per_10_fail')
            self.pc_per_fail()

    def pc_per_success(self):
        pass

    def pc_per_fail(self):
        pass

        
        print('To be continued...')

    def combat_1(self):
        #this will be a new chapter inside the level
        pass