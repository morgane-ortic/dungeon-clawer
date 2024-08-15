from utils import Fore, Style
from character import Character

class PC(Character):
    '''Character class to store the character's data'''

    def __init__(self, sheet_path):
        '''Initialise the class with character's data from read_char_sheet'''
        # Inherit the init method from the parent class Character
        super().__init__(sheet_path)
        # Call read_char_sheet method to get both general and PC specific character's attributes
        self._read_char_sheet()


    def _read_char_sheet(self):
        '''Read the data and get character's stats from the character sheet'''
        # Inherit the instance attributes (characteristics) from the parent class Character
        super()._read_char_sheet()

        # unpack the dictionary to get the additional PC data
        self.char_class = self.char_dictionary['char_class']
        self.species = self.char_dictionary['species']
        self.save_bonuses = self.char_dictionary['abilities_and_bonuses']['save_bonuses']
        self.eq_weapon = self.char_dictionary['equipment'][0]['weapons'][0]
        self.eq_armor = self.char_dictionary['equipment'][0]['armor'][0]


    def print_char_sheet(self, abilities_bonus_values=[]):
        '''Print the character sheet'''
        # Create a list of ability bonuses (to be displayed later)
        self.abilities_bonus_values = abilities_bonus_values
        # Append each ability bonuses to the list
        for ability, value in self.abilities_bonuses.items():
            self.abilities_bonus_values.append(value)

        # Print the character's sheet
        print(Fore.RED + f'{self.name.upper()}' + Style.RESET_ALL)
        print(f'\nClass: {self.format_string(self.char_class)}')
        print(f'Species: {self.format_string(self.species)}')
        print(f'\nArmor Class: {self.ac}')
        print(f'Hit Points: {self.hp}')
        print(f'Proficiency: {self.pp}')
        print ('\nAbilities:')
        # Print every ability + value + associated bonus from our abilities_bonus_values list
        for ability, value in self.abilities.items():
            formatted_ability = self.format_string(ability)
            print(f'    {formatted_ability}: {value} ({self.abilities_bonuses[ability]})')
        print('\nSave Bonuses:')
        # Print every save bonus + value
        for ability, value in self.save_bonuses.items():
            formatted_ability = self.format_string(ability)
            print(f'    {formatted_ability}: {value}')        
        print(f'Passive Wisdom (Perception):{self.pp}')
        print('\nSkills:')
        # Print every skill + value
        for skill, value in self.skills.items():#
            formatted_skill = self.format_string(skill)
            print(f'    {formatted_skill}: {value}')
        print(f'\nWeapon equipped: {self.format_string(self.eq_weapon)}')
        print(f'Armor equipped: {self.format_string(self.eq_armor)}\n')