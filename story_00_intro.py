from utils import Fore, Style, prints, prints_plus, sleep, slow_text_delay

# Most text is printed in typewriting style using prints, defined in utils.py

def story_intro():
    '''Print the story's introduction'''
    prints_plus('Ortic productions present\n')
    prints_plus(Fore.RED + '          KARLACH' + Style.RESET_ALL)
    prints_plus('            in\n')
    prints_plus(Fore.RED + 'D U N G E O N   C L A W E R\n' + Style.RESET_ALL, slow_text_delay)
    sleep(0.8)
    input('Press Enter to start the game...\n')

def main_menu():
    main_menu_choices = [
        'Start game story',
        'Arena',
        'See character sheet',
        'Exit game\n'
    ]
    for index, choice in enumerate(main_menu_choices):
        print(f'{index + 1}. {choice}')

    menu_choice = int(input('Enter your choice: '))
    return menu_choice