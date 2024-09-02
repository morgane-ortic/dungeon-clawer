from character import PC, NPC
from utils import sleep

def combat (pc, npc):
    print('It\'s a fight!')
    sleep(1)
    print(f'''
{pc.name}: {pc.hp} HP
{npc.name}: {npc.hp} HP
''')
    pc_init = pc.roll_initiative()
    npc_init = npc.roll_initiative()
    if pc_init > npc_init:
        p1 = pc
        p2 = npc
    else:
        p1 = npc
        p2 = pc
    print(f'{p1.name} is starting')
    input('...')
    while p1.hp > 0 and p2.hp > 0:
        p1.atk_roll(p2)
        if p2.hp <= 0:
            break
        p2.atk_roll(p1)
        if p1.hp <= 0:
            break
        