import json

class Character:
    def __init__(self, name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, weapon, armor):
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
        self.abilities_bonus_values = abilities_bonus_values
        for ability, value in self.abilities_bonuses.items():
            self.abilities_bonus_values.append(value)
        print(f'Name: {self.name.upper()}')
        print(f'\nArmor Class: {self.ac}')
        print(f'\nHit Points: {self.hp}')
        print ('\nAbilities:')
        for ability, value in self.abilities.items():
            print(f'    {ability}: {value} ({self.abilities_bonuses[ability]})')
        print('\nSave Bonuses:')
        for ability, value in self.save_bonuses.items():
            print(f'    {ability}: {value}')
        print('\nSkills:')
        for skill, value in self.skills.items():
            print(f'    {skill}: {value}')
        print(f'\nWeapon equipped: {self.weapon}')
        print(f'\nArmor equipped: {self.armor}')


def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    

def read_char_sheet(char_sheet):
    '''Read the data from the character sheet for later use (name, abilities, skills...)'''
    char_dictionary = char_sheet[0] # Accesses the dictionary with the character's data
    name = char_dictionary['name']
    hp = char_dictionary['hp']
    ac = char_dictionary['ac']
    abilities = char_dictionary['abilities_and_bonuses']['abilities']
    abilities_bonuses = char_dictionary['abilities_and_bonuses']['abilities_bonuses']
    save_bonuses = char_dictionary['abilities_and_bonuses']['save_bonuses']
    skills = char_dictionary['skills']
    weapon = char_dictionary['equipment'][0]['weapons'][0]
    armor = char_dictionary['equipment'][0]['armor'][0]
    
    return name, ac, hp, abilities, abilities_bonuses, save_bonuses, skills, weapon, armor

    
def main():
    char_sheet = read_json_file('char_sheet.json')
    # assign the variables from the character sheet to a tuple char_data
    char_data = read_char_sheet(char_sheet) 
    # instantiate the PC unpack the tuple with the character's data
    pc = Character(*char_data)

    # print the character's sheet
    pc.print_char_sheet()
    

if __name__ == '__main__':
    main()