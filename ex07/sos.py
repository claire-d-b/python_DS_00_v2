from sys import argv

NESTED_MORSE = {
    ' ': '/',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def main():
    """This program takes on argument and uses a dictionary to store
morse code. It processes only spaces and alnum characters. It outputs
the argument encoded in morse code."""
    key = 0
    args = []
    kwargs = {}

    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

    try:
        assert len(args) == 1
        for arg in args:
            for letter in arg:
                assert letter.isalnum()
    except AssertionError:
        raise AssertionError("the arguments are bad")
    for arg in args:
        for letter in arg:
            if letter.isdigit():
                print(NESTED_MORSE[letter], end=" ")
            else:
                print(NESTED_MORSE[letter.upper()], end=" ")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
