import random
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

    while pc.hp and npc.hp < 0:
        p1.attack(p2)
        p2.attack(p1)