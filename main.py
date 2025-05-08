from time import sleep
from arena import arena
from utils import clear, prints, prints_plus
from character import PC, NPC
from combat import combat
from game_lines import unavailable_feature
from story_00_intro import story_intro, main_menu
from story_01 import init_dialogs as init_dialogs_01, wake_up

what_do = 'What do you do? '


def main():
    clear()       
    story_intro()


    pc = PC('char_sheet.json')


    while True:
        choice = main_menu()
        if choice == 1:

            # clear the terminal after each part/sub-part
            clear()
            # Initialize all dialogs for the next area
            init_dialogs_01()
            wake_up(pc)
        elif choice == 2:
            arena(pc)
        elif choice == 3:
            print('''

''')
            pc.print_char_sheet()
        elif choice == 4:
            prints_plus('Exiting game............', 0.05)
            exit()
        else:
            prints('Invalid choice. Please try again.\n')



   
    

if __name__ == '__main__':
    main()