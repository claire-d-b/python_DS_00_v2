from sys import argv
from ft_filter import ft_filter


def is_chars(chars: any):
    """Count occurences of chars"""
    try:
        str(chars)
        return True
    except ValueError:
        return False


def is_digit(chars: any):
    """Count occurences of digits"""
    try:
        int(chars)
        return True
    except ValueError:
        return False


def main():
    """Program that outputs a list of words from S that have a length\
greater than N. This is performed by custom filter function.
Builtin python filter result and docstring is shown for comparison."""
    args = argv[1:]

    try:
        assert len(args) == 2, "the arguments are bad"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return
    else:
        try:
            assert is_chars(args[0]), "the arguments are bad"
            assert is_digit(args[1]), "the arguments are bad"
        except AssertionError as e:
            print(f"AssertionError: {e}")
            return
    words = args[0].split()
    n = int(args[1])
    print(ft_filter(lambda word: len(word) >= n, words))
    print(filter(lambda word: len(word) >= n, words))
    print(list(ft_filter(lambda word: len(word) >= n, words)))
    print(list(filter(lambda word: len(word) >= n, words)))
    print(ft_filter.__doc__)
    print(filter.__doc__)


if __name__ == "__main__":
    main()
