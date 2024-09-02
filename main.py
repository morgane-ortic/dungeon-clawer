from utils import *
from character import PC, NPC
from combat import combat
from story_0_intro import story_intro


def main():
    clear()
    # instantiate the PC with the proper character sheet file as argument
    pc = PC('char_sheet.json')
    goblin = NPC('npcs.json')
    # story_intro()

    # clear the terminal after each part/sub-part
    clear()

    while True:
        menu_choice = input('''1. Show your character's sheet
2. Show enemy's character sheet
3. Pick up a fight with a nasty goblin!
''')
        
        if menu_choice == '1':
            clear()
            # print the character's sheet
            pc.print_char_sheet()
        elif menu_choice == '2':
            clear()
            # print the enemy's sheet
            goblin.print_char_sheet()
        elif menu_choice == '3':
            clear()
            combat(pc, goblin)
        else:
            wrong_choice
    

if __name__ == '__main__':
    main()