from utils import *
from character import PC, NPC
from combat import combat
from story_00_intro import story_intro
from story_01 import init_dialogs as init_dialogs_01, wake_up

what_do = 'What do you do? '

def main():
    clear()
    # instantiate the PC with the proper character sheet file as argument
    pc = PC('char_sheet.json')
    pc.print_char_sheet()
    input('')
    
    # story_intro()

    # clear the terminal after each part/sub-part
    clear()
    # Initialize all dialogs for the next area
    init_dialogs_01()
    wake_up()

   
    

if __name__ == '__main__':
    main()