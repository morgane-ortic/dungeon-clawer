from time import sleep
from arena import arena
from utils import clear, prints, prints_plus
from character import PC, NPC
from combat import combat
from game_lines import unavailable_feature
from story_00_intro import story_intro, main_menu
from story_01 import LevelStory01

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
            story_01 = LevelStory01(pc)
            story_01.wake_up()
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