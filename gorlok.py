import sys
import time
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
print("\033[1;31m- Welcome to Gorlok: Origins of Icram -\033[0m")
print()
intro_dialogue_seq = [
    {'type': 'narrate', 'text': "The Narrator stands over you as you open your weary eyes\n"},
    {'type': 'text', 'text': "..."}
]

mixed_type(intro_dialogue_seq)

time.sleep(1)

type_text("\n\nNarrator: ")
type_dialogue("You have to fight Gorlok right now. Sorry bro!")
print("\n")

time.sleep(1)

# run_battle()
test_battle()

def test_dummy():
    pass