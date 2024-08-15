from colorama import Fore, Style
from character import Character

class NPC(Character):
    '''NPC subclass for getting and using NPCs characteristics'''
    
    def __init__(self, sheet_path):
        '''Initialise the class with NPC's data from read_char_sheet'''
        # Inherit the init method from the parent class Character
        super().__init__(sheet_path)
        # Call read_char_sheet method to get both general and NPC specific character's attributes
        self._read_char_sheet()


    def _read_char_sheet(self):
        '''Read the data and get NPC's stats from the character sheet'''
        # Inherit the instance attributes (characteristics) from the parent class Character
        super()._read_char_sheet()

        # unpack the dictionary to get the additional NPC data
        self.id = self.char_dictionary['id']
        self.xp = self.char_dictionary['xp']
        self.attacks = self.char_dictionary['attacks']
    

    def print_char_sheet(self, abilities_bonus_values=[]):
        '''Print the NPC's sheet'''
        # Create a list of ability bonuses (to be displayed later)
        self.abilities_bonus_values = abilities_bonus_values
        # Append each ability bonuses to the list
        for ability, value in self.abilities_bonuses.items():
            self.abilities_bonus_values.append(value)
        # convert all attacks to a list to access them easily
        attacks_list = list(self.attacks.items())

        # Print the character's sheet
        print(Fore.GREEN + f'{self.name.upper()}' + Style.RESET_ALL)
        print(f'\nArmor Class: {self.ac}')
        print(f'Hit Points: {self.hp}')

        print ('\nAbilities:')
        # Print every ability + value + associated bonus from our abilities_bonus_values list
        for ability, value in self.abilities.items():
            formatted_ability = self.format_string(ability)
            print(f'    {formatted_ability}: {value} ({self.abilities_bonuses[ability]})')
        print(f'\nPassive Wisdom (Perception): {self.pp}')

        print('\nSkills:')
        # Print every skill + value
        for skill, value in self.skills.items():#
            formatted_skill = self.format_string(skill)
            print(f'    {formatted_skill}: {value}')

        print(f'\nXP: {self.xp}')

        print(f'\nAttacks:')
        print(f'    {attacks_list}')
        print('\n========================================================================')