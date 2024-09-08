from sys import argv


def main():
    args = []
    kwargs = {}
    key = 0
    """ catches program argument """
    for arg in argv[1:]:
        value = arg
        kwargs[key] = value
        args.append(arg)
        key += 1

    if len(args) > 1:
        raise AssertionError("more than one argument is provided")

    """ check whether arg is valid and is an even/odd number """

    try:
        if abs(int(arg)) % 2:
            print("I'm Odd")
        else:
            print("I'm Even")
    except ValueError as e:
        raise AssertionError("argument is not an integer")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
