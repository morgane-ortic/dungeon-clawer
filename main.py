from time import sleep
from arena import arena
from utils import clear, prints, prints_plus, printy
from character import PC, NPC
from combat import combat
from game_lines import unavailable_feature
from story_00_intro import story_intro, main_menu
from story_01 import LevelStory01


def main():
    clear()       
    # story_intro()


    pc = PC('char_sheet.json')


    while True:
        choice = main_menu()
        if choice == '1':
            # clear the terminal after each part/sub-part
            clear()
            story_01 = LevelStory01(pc)
            story_01.wake_up()
        elif choice == '2':
            clear()
            arena(pc)
        elif choice == '3':
            clear()
            print('\n                            CHARACTER SHEET')
            pc.print_char_sheet()
            clear()
        elif choice == '4':
            prints_plus('Exiting game............', 0.05)
            exit()
        else:
            clear()
            sleep(0.2)
            printy('\nInvalid choice. Please try again.\n')



   
    

if __name__ == '__main__':
    main()