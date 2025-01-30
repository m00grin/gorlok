import sys
import time

def type_narrate(text, delay=0.06):
    for char in text:
        sys.stdout.write("\033[3m" + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)

def type_dialogue(text, delay=0.06):
    sys.stdout.write('"')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('"')
    sys.stdout.flush()

def type_text(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('')
    sys.stdout.flush()

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


intro_dialogue_seq = [
    {'type': 'text', 'text': "Narrator: "},
    {'type': 'narrate', 'text': "The Narrator stands over you as you open your weary eyes."},
    {'type': 'text', 'text': "..."}
]

mixed_type(intro_dialogue_seq)