# namedtuple will easy up recovering the dice results
from collections import namedtuple
from colorama import Fore, Style
import json
import os
from random import randint
import sys
from time import sleep

slow_text_delay = 0.15

# Global variable to store dialogs
dialogs = {}


def read_json_file(file_path):
    '''Read the data from a json file'''
    with open(file_path, 'r') as file:
        return json.load(file)
    
#========================DIALOG FUNCTIONS========================
    
def prints(text, delay=0.05):
    '''Print text with a typewriter effect'''
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    input('\n...')
    
def prints_plus(text, delay = 0.15):
    '''slower prints (by default) without input at the end'''
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(delay)
    print()  # Move to the next line after printing the text

def printy(text, color=Fore.YELLOW):
    print(color + text + Style.RESET_ALL)


def load_dialogs(file_path):
    '''Load the data from appropriate json file and store it in the global variable'''
    global dialogs
    loaded_dialogs = read_json_file(file_path)
    if not dialogs:
        dialogs = loaded_dialogs
    # if dialogs are already loaded, add new ones to dialogs
    else:
        dialogs.update(loaded_dialogs)

def get_char_dialog(character):
    '''get all dialogs for each character'''
    return dialogs.get(character, {})

def dprint(dialog_key="ERROR: DIALOG NOT FOUND", character='narrator'):
    '''Print a specific dialog line for a character'''
    dialog = get_char_dialog(character).get(dialog_key, "")

    prints(dialog)


def clear():
    os.system('cls||clear')

#========================GAMEPLAY FUNCTIONS========================

Result = namedtuple('Result', ['base_result', 'result'])

def roll_dice(faces=20, bonus=0):
    base_result = randint(1, faces)
    result = base_result + bonus
    return Result(base_result, result)