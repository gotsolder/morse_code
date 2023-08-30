import re

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

#  −− −−− ·−· ··· ·    −·−· −−− −·· ·
#  M   O   R   S  E     C    O   D  E

while True:
    user_input = input("\nEnter string to be converted: ").upper().strip()
    is_ascii = re.search("[A-Z0-9]", user_input[0])
    if is_ascii:
        lookup = CODE
        word_list = user_input.split()
        end = " "
    else:
        lookup = CODE_REVERSED
        word_list = user_input.split(" " * 4)
        end = ""

    for word in word_list:
        if not is_ascii:  word = word.split()
        for index, char in enumerate(word):
            if char in lookup.keys():
                if index == 0:
                    print(lookup[char], end=end)
                else:
                    print(lookup[char].lower(), end=end)
            else:
                raise Exception(f"Sorry, '{char}' is not in the morse code definition")

        print(" ", end="")
        if is_ascii: print("  " * 3, end="")


