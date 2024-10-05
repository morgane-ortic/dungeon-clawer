from time import sleep

from character import PC, NPC
from combat import combat
from utils import clear, read_json_file, text_to_snake_case

def list_enemies():
    npc_names = []
    npcs_data = read_json_file('npcs.json')
    for npc in npcs_data:
        npc_names.append(npc['name'])
    return npc_names

def arena():
    pc = PC('char_sheet.json')
    npc_names = list_enemies()

    while True:
        clear()
        npc_names_str = '\n'.join(npc_names)
        enemy_choice = input(f'''ARENA MODE
            
Type the name of the enemy you wish to fight:
            
{npc_names_str}

''')
    
        while not any(enemy_choice.lower() == npc.lower() for npc in npc_names):
            enemy_choice = input("\nInvalid choice. Please select a valid enemy name:\n")

        npc_id = text_to_snake_case(enemy_choice)
        input(f"\nYou are fighting {enemy_choice}...\n")
        npc = NPC('npcs.json', npc_id)
        combat(pc, npc)
        break