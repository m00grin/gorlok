import sys
import time

STYLES = {
    "bold": "\033[1m",
    "italic": "\033[3m",
    "underline": "\033[4m",
    "blink": "\033[5m",
    "red": "\033[1;31m",
    "dimmed": "\033[2m",
}

def styled_text(text, style=None):
    return f"{STYLES.get(style, '')}{text}{STYLES['reset']}" if style else text

def typewriter(text, speed=0.05):
    for char in styled:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()