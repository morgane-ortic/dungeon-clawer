from utils import *
from character import Character
from story_0_intro import story_intro
    

def read_char_sheet(char_sheet):
    '''Read the data from the character sheet for later use (name, abilities, skills...)'''
    # Access the dictionary with the character's data
    char_dictionary = char_sheet[0]
    # Unpack the dictionary to get all the character's data
    name = char_dictionary['name']
    hp = char_dictionary['hp']
    ac = char_dictionary['ac']
    abilities = char_dictionary['abilities_and_bonuses']['abilities']
    abilities_bonuses = char_dictionary['abilities_and_bonuses']['abilities_bonuses']
    save_bonuses = char_dictionary['abilities_and_bonuses']['save_bonuses']
    skills = char_dictionary['skills']
    weapon = char_dictionary['equipment'][0]['weapons'][0]
    armor = char_dictionary['equipment'][0]['armor'][0]
    
    # Return the character's data as a tuple
    return name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, weapon, armor

    
def main():
    # read the character sheet from the json file
    char_sheet = read_json_file('char_sheet.json')
    # assign the variables from the character sheet to a tuple char_data
    char_data = read_char_sheet(char_sheet) 
    # instantiate the PC with the character's data as arguments
    # *char_data unpacks the tuple to pass the individual variables
    pc = Character(*char_data)
    story_intro()

    # print the character's sheet
    pc.print_char_sheet()
    

if __name__ == '__main__':
    main()