class Character:
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

    def print_char_sheet(self, abilities_bonus_values=[]):
        '''Print the character sheet'''
        # Create a list of ability bonuses (to be displayed later)
        self.abilities_bonus_values = abilities_bonus_values
        # Append each ability bonuses to the list
        for ability, value in self.abilities_bonuses.items():
            self.abilities_bonus_values.append(value)
        # Print the character's sheet
        print(f'Name: {self.name.upper()}')
        print(f'\nArmor Class: {self.ac}')
        print(f'\nHit Points: {self.hp}')
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
        print(f'\nArmor equipped: {self.armor}')