

class NPC:
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