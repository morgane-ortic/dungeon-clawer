import re
from time import sleep
from colorama import Fore, Style
from utils import prints, printy, read_json_file, roll_dice, sleep

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
        for ability, value in self.abilities:
            setattr(self, ability, value)
        print(self.strength)
        print(self.dexterity)

        self.abilities_bonuses = self.char_dictionary['abilities_and_bonuses']['abilities_bonuses']
        self.str_bns= self.abilities_bonuses['strength']
        self.dex_bns = self.abilities_bonuses['dexterity']
        self.con_bns = self.abilities_bonuses['constitution']
        self.int_bns = self.abilities_bonuses['intelligence']
        self.wis_bns = self.abilities_bonuses['wisdom']
        self.cha_bns = self.abilities_bonuses['charisma']

        self.skills = self.char_dictionary['skills']
        self.pp = self.char_dictionary['pp']

        # We don't need to return any variable here, as the variables we'll need are now instance attributes

    def format_string(self, s: str) -> str:
        '''We format each string on the fly by calling this method in print_char_sheet
        If later the formatted strings are needed in more places: create variables to store them
        Maybe move this method to utils.py if it's used in more files'''
        return re.sub(r'_+', ' ', s).title()

    def roll_initiative(self):
        input('Roll for Initiative [ENTER]:')
        sleep(1)
        roll = roll_dice(20, self.initiative)
        prints('......')
        print(f'{self.name} rolls {roll.base_result} + {self.initiative} = {roll.result}')


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
        self.str_sv_bns= self.save_bonuses['strength']
        self.dex_sv_bns = self.save_bonuses['dexterity']
        self.con_sv_bns = self.save_bonuses['constitution']
        self.int_sv_bns = self.save_bonuses['intelligence']
        self.wis_sv_bns = self.save_bonuses['wisdom']
        self.cha_sv_bns = self.save_bonuses['charisma']

        # Now get all the equipment stats
        # Fetch the first key-value pair from the weapons dictionary
        eq_weapon_pair = next(iter(self.char_dictionary['equipment'][0]['weapons'].items()))
        # Assign the key (name) and value (stats) to separate variables
        self.eq_weapon, self.eq_weapon_stats = eq_weapon_pair
        self.atk_range = self.eq_weapon_stats[0]
        self.atk_bonus = self.abilities_bonuses[self.eq_weapon_stats[1]] + self.proficiency
        self.dmg_dice = self.eq_weapon_stats[2]
        self.dmg_bonus = self.eq_weapon_stats[3]
        eq_armor_pair = next(iter(self.char_dictionary['equipment'][0]['armor'].items()))
        self.eq_armor, self.eq_armor_stats = eq_armor_pair
        self.attack = ""

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
        print(f'Proficiency: {self.proficiency}')
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

    def atk_roll(self, target):
        '''PC rolls for attack to know whether they hit'''
        input('Press ENTER to attack')
        # calculate roll result
        roll = roll_dice(20, self.atk_bonus)
        prints('....')
        # display roll result
        print(f'You roll {roll.base_result} + {self.atk_bonus} = {roll.result}')
        # if target is hit, continue to damage roll
        if roll >= target.ac:
            print(f'You hit {target.name}!')
            sleep(0.5)
            self.dmg_roll()
        # if target is missed, stop the character's turn without dealing damage
        else:
            print('You miss')

    def dmg_roll(self, target):
        '''PC rolls for damage (hit points) dealt to enemy'''
        input('Press ENTER to roll for damage')
        # calculate roll result
        roll = roll_dice(self.dmg_dice, self.dmg_bonus)
        prints('....')
        # display roll result
        print(f'You roll {roll.base_result} + {self.dmg_bonus} = {roll.result}')
        # call take_damage() for target to apply damage to target
        target.take_damage(roll.result)

    def take_damage(self, damage):
        '''Apply damage to PC when hit'''
        self.hp -= damage
        if self.hp <= 0:
            print(f"You fall unconscious on the ground.")
        else:
            print(f"You take {damage} damage! {self.health} HP remaining.")



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
        # store attack bonus + damage. Only for the first weapon for now. (will be automatically used in combat)
        self.atk_bns = self.attacks
        self.main_atk, self.main_atk_stats = next(iter(self.attacks.items()))
        self.atk_bns, self.dmg = self.main_atk_stats


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


    def attack(self, target):
        '''NPC rolls for damage (hit points) dealt to enemy'''
        print(f'{self.name} attacks!')
        # calculate roll result
        roll = roll_dice(20, self.atk_bonus)
        prints('....')
        # display roll result
        print(f'{self.name} rolls {roll.result}')
        # if target is hit, apply fixed damage value
        if roll >= target.ac:
            print(f'{self.name} hits {target.name}!')
            sleep(0.5)
            # For NPCs, damage dealt is always the self.damage value (fixed damage)
            print(f'{target.name} takes {self.dmg} damage.')
            # call take_damage() for target to apply damage to target
            target.take_damage(self.dmg)
        # if target is missed, stop the character's turn without dealing damage
        else:
            print(f'{self.name} misses')