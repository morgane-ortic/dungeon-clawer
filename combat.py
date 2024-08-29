import random
from character import PC, NPC

def combat (pc, npc):
    while pc.hp and npc.hp < 0:
        pass