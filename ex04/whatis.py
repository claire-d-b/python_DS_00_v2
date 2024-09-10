from sys import argv


def main():
    """Program that outputs if given number is odd or even"""
    args = []
    kwargs = {}
    key = 0
    # catches program arguments
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

    if len(args) == 0 or len(args) > 1:
        raise AssertionError("Incorrect number of arguments")

    # check whether arg is valid and is an even/odd number

    try:
        if abs(int(arg)) % 2:
            print("I'm Odd")
        else:
            print("I'm Even")
    except ValueError:
        raise AssertionError("argument is not an integer")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
