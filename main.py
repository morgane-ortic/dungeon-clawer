from utils import *
from character import Character
from story_0_intro import story_intro
import os # not sure if will be used, mqybe remove later

    
def main():
    # read the character sheet from the json file
    char_sheet = read_json_file('char_sheet.json')
    # instantiate the PC with the character's data as arguments
    # *char_data unpacks the tuple to pass the individual variables
    pc = Character.read_char_sheet(char_sheet)
    story_intro()

    # print the character's sheet
    pc.print_char_sheet()
    

if __name__ == '__main__':
    main()