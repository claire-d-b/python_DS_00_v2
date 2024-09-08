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
    key = 0
    args = []
    kwargs = {}
    """ catches program argument """
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

    try:
        assert len(args) == 1, "the arguments are bad"
        for arg in args:
            for letter in arg:
                assert letter.isalnum(), "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    for arg in args:
        for letter in arg:
            if letter.isdigit():
                print(NESTED_MORSE[letter], end="")
            else:
                print(NESTED_MORSE[letter.upper()], end="")


if __name__ == "__main__":
    main()
