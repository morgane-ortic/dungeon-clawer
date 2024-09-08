from utils import *
from character import PC, NPC
from combat import combat
from story_00_intro import story_intro


def main():
    clear()
    # instantiate the PC with the proper character sheet file as argument
    pc = PC('char_sheet.json')
    
    story_intro()

    # clear the terminal after each part/sub-part
    clear()

   
    

if __name__ == '__main__':
    main()