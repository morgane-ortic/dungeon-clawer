from utils import read_json_file
import re

class Character:
    '''Character class to store the character's data'''

    def __init__(self, sheet_path):
        '''Initialise the class with character's data from read_char_sheet'''
        self.char_sheet = read_json_file(sheet_path)
        # Get character data from the character sheet by calling the read_char_sheet() method
        self._read_char_sheet()


    # The method is private as it only needs to be accessed from other methods inside the class
    def _read_char_sheet(self):
        '''Read the data and get character's stats from the character sheet'''
        # access the dictionary with the character's data
        self.char_dictionary = self.char_sheet[0]
        
        # unpack the dictionary to get all the character's data
        self.name = self.char_dictionary['name']
        self.hp = self.char_dictionary['hp']
        self.ac = self.char_dictionary['ac']
        self.proficiency = self.char_dictionary['abilities_and_bonuses']['proficiency']
        self.abilities = self.char_dictionary['abilities_and_bonuses']['abilities']
        self.abilities_bonuses = self.char_dictionary['abilities_and_bonuses']['abilities_bonuses']
        self.skills = self.char_dictionary['skills']
        self.pp = self.char_dictionary['pp']

        # We don't need to return any variable here, as the variables we'll need are now instance attributes
    

    def format_string(self, s: str) -> str:
        '''We format each string on the fly by calling this method in print_char_sheet
        If later the formatted strings are needed in more places: create variables to store them
        Maybe move this method to utils.py if it's used in more files'''
        return re.sub(r'_+', ' ', s).title()