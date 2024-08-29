from colorama import Fore, Style
import json
import os
from random import randint
import sys
from time import sleep

slow_text_delay = 0.15

def read_json_file(file_path):
    '''Read the data from a json file'''
    with open(file_path, 'r') as file:
        return json.load(file)
    
def prints(text, delay=0.05):
    '''Print text with a typewriter effect'''
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()  # Move to the next line after printing the text

def wrong_choice():
    '''Default message when a wrong choice in inputed by player'''
    prints(Fore.RED + 'WRONG ANSWER! Please enter a valid choice:\n' + Style.RESET_ALL, slow_text_delay)

def clear():
    os.system('cls||clear')

def roll_dice(faces=20, bonus=0):
    roll_result = randint(1, faces)
    result = roll_result + bonus
    return roll_result, result