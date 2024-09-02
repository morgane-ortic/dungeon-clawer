from character import PC, NPC
from utils import roll_dice

def combat (pc, npc):
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
        