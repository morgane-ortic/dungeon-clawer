from utils import Fore, Style
class Character:
    '''Character class to store the character's data'''

    def __init__(self, name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, pp, weapon, armor):
        '''Initialise the class with character's data from read_char_sheet'''
        self.name = name
        self.ac = ac
        self.hp = hp
        self.abilities = abilities
        self.abilities_bonuses = abilities_bonuses
        self.save_bonuses = save_bonuses
        self.skills = skills
        self.pp = pp
        self.weapon = weapon
        self.armor = armor


    # We make read_char_sheet a class method
    # So that it's better encapsulated in the Character class but we can use it without instantiating the class
    @classmethod
    def read_char_sheet(cls, char_sheet):
        '''Read the data and get character's stats from the character sheet'''
        # access the dictionary with the character's data
        char_dictionary = char_sheet[0]
        # unpack the dictionary to get all the character's data
        name = char_dictionary['name']
        hp = char_dictionary['hp']
        ac = char_dictionary['ac']
        abilities = char_dictionary['abilities_and_bonuses']['abilities']
        abilities_bonuses = char_dictionary['abilities_and_bonuses']['abilities_bonuses']
        save_bonuses = char_dictionary['abilities_and_bonuses']['save_bonuses']
        skills = char_dictionary['skills']
        pp = char_dictionary['pp']
        weapon = char_dictionary['equipment'][0]['weapons'][0]
        armor = char_dictionary['equipment'][0]['armor'][0]
        
        # return the character's data as a tuple
        return cls(name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, pp, weapon, armor)


    def print_char_sheet(self, abilities_bonus_values=[]):
        '''Print the character sheet'''
        # Create a list of ability bonuses (to be displayed later)
        self.abilities_bonus_values = abilities_bonus_values
        # Append each ability bonuses to the list
        for ability, value in self.abilities_bonuses.items():
            self.abilities_bonus_values.append(value)
        # Print the character's sheet
        print(Fore.RED + f'{self.name.upper()}' + Style.RESET_ALL)
        print(f'\nArmor Class: {self.ac}')
        print(f'Hit Points: {self.hp}')
        print ('\nAbilities:')
        # Print every ability + value + associated bonus from our abilities_bonus_values list
        for ability, value in self.abilities.items():
            print(f'    {ability}: {value} ({self.abilities_bonuses[ability]})')
        print('\nSave Bonuses:')
        # Print every save bonus + value
        for ability, value in self.save_bonuses.items():
            print(f'    {ability}: {value}')
        print('\nSkills:')
        # Print every skill + value
        for skill, value in self.skills.items():
            print(f'    {skill}: {value}')
        print(f'Passive perception: {self.pp}')
        print(f'\nWeapon equipped: {self.weapon}')
        print(f'Armor equipped: {self.armor}')


# class Character:
    '''Character class to store the character's data'''

    def __init__(self, name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, weapon, armor):
        '''Initialise the class with character's data from read_char_sheet'''
        self.name = name
        self.ac = ac
        self.hp = hp
        self.abilities = abilities
        self.abilities_bonuses = abilities_bonuses
        self.save_bonuses = save_bonuses
        self.skills = skills
        self.weapon = weapon
        self.armor = armor


    # We make read_char_sheet a class method
    # So that it's better encapsulated in the Character class but we can use it without instantiating the class
    @classmethod
    def read_char_sheet(cls, char_sheet):
        '''Read the data and get character's stats from the character sheet'''
        # access the dictionary with the character's data
        char_dictionary = char_sheet[0]
        # unpack the dictionary to get all the character's data
        name = char_dictionary['name']
        hp = char_dictionary['hp']
        ac = char_dictionary['ac']
        abilities = char_dictionary['abilities_and_bonuses']['abilities']
        abilities_bonuses = char_dictionary['abilities_and_bonuses']['abilities_bonuses']
        save_bonuses = char_dictionary['abilities_and_bonuses']['save_bonuses']
        skills = char_dictionary['skills']
        weapon = char_dictionary['equipment'][0]['weapons'][0]
        armor = char_dictionary['equipment'][0]['armor'][0]
        
        # return the character's data as a tuple
        return cls(name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, weapon, armor)


    def print_char_sheet(self, abilities_bonus_values=[]):
        '''Print the character sheet'''
        # Create a list of ability bonuses (to be displayed later)
        self.abilities_bonus_values = abilities_bonus_values
        # Append each ability bonuses to the list
        for ability, value in self.abilities_bonuses.items():
            self.abilities_bonus_values.append(value)
        # Print the character's sheet
        print(Fore.RED + f'{self.name.upper()}' + Style.RESET_ALL)
        print(f'\nArmor Class: {self.ac}')
        print(f'Hit Points: {self.hp}')
        print ('\nAbilities:')
        # Print every ability + value + associated bonus from our abilities_bonus_values list
        for ability, value in self.abilities.items():
            print(f'    {ability}: {value} ({self.abilities_bonuses[ability]})')
        print('\nSave Bonuses:')
        # Print every save bonus + value
        for ability, value in self.save_bonuses.items():
            print(f'    {ability}: {value}')
        print('\nSkills:')
        # Print every skill + value
        for skill, value in self.skills.items():
            print(f'    {skill}: {value}')
        print(f'\nWeapon equipped: {self.weapon}')
        print(f'Armor equipped: {self.armor}')