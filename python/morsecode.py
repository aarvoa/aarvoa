import time
import winsound

# Morse code timings (in milliseconds)
DOT_DURATION = 150
DASH_DURATION = DOT_DURATION * 3
SYMBOL_GAP = DOT_DURATION / 1000  # Gap between dots/dashes inside a letter (seconds)

def play_morse_sound(morse_string):
    for char in morse_string:
        if char == '.':
            winsound.Beep(750, DOT_DURATION)
            time.sleep(SYMBOL_GAP)
        elif char == '-':
            winsound.Beep(750, DASH_DURATION)
            time.sleep(SYMBOL_GAP)
        elif char == ' ':
            # Gap between words/letters
            time.sleep(DOT_DURATION * 3 / 1000)

morse_code_map = {
    # Letters
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    
    # Numerals
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '
}

sentence = input("Enter your Sentence!: ")
morse_code = ""

for i in sentence:
    u = i.upper()
    val = morse_code_map[u]
    morse_code = morse_code + val

print(morse_code)
play_morse_sound(morse_code)




