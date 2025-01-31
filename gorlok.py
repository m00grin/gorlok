import sys
import time
import pyfiglet
from art import text2art
from colorama import Fore, Back, Style
from battles.final_battle import run_battle
from battles.battle_tester import test_battle

def type_narrate(text, delay=0.05):
    for char in text:
        
        sys.stdout.write("\033[3m" + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

def type_dialogue(text, delay=0.03):
    sys.stdout.write('"')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('"')
    sys.stdout.flush()

def type_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
    sys.stdout.write('')

def mixed_type(lines):
    for line in lines:
        line_type = line['type']
        text = line['text']

        if line_type == 'narrate':
            type_narrate(text)
        elif line_type == 'dialogue':
            type_dialogue(text)
        elif line_type == 'text':
            type_text(text)

        if "..." in text:
            time.sleep(1)
print("\n")
ascii_gorlok = text2art("GORLOK:")
ascii_icram = text2art("ORIGINS OF ICRAM")
print(Fore.RED + ascii_gorlok + Style.RESET_ALL)  # Red text
print(Fore.YELLOW + ascii_icram + Style.RESET_ALL)  # Yellow text

print()
intro_dialogue_seq_1 = [
    {'type': 'narrate', 'text': "The Narrator stands over you as you regain consciousness\n"},
    {'type': 'text', 'text': "...\n"},
    {'type': 'narrate', 'text': "You rub your eyes and take a look around... "},
    {'type': 'narrate', 'text': "The ground starts to tremble beneath you, and the glint of an axe swings into view\n\n"},
    {'type': 'narrate', 'text': "Almost involuntarily, you roll to the side, narrowly avoiding the axe's deadly arc\n\n"},
    {'type': 'narrate', 'text': "You look up to see a massive figure standing over you, a hulking beast with a twisted grin\n\n"},
    {'type': 'text', 'text': "\nThe Narrator: "},
    {'type': 'dialogue', 'text': "Get up! Strike down Gorlok before he can swing the Nether Axe again!"},
    {'type': 'text', 'text': "\n\n\n"},
]

mixed_type(intro_dialogue_seq_1)

time.sleep(1)

time.sleep(1)

# run_battle()
test_battle()