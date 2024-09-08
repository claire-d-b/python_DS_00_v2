from sys import argv


def main():
    punctuation = {'.', ',', ';', ':', '!', '?', '\'', '"', '(', ')',
                   '[', ']', '{', '}', '-', '_', '/', '\\', '|', '@',
                   '#', '$', '%', '^', '&', '*', '<', '>', '~', '`'}

    spaces = {'\t', '\n', '\r', '\v', '\f', ' ', ''}

    try:
        len(argv[1:]) == 0 or len(argv[1:]) == 1, "Wrong number of arguments"
    except AssertionError as e:
        print(f"AssertionError: {e}")

    carriage_ret = 0


# CtrlC tells the terminal to send a SIGINT to the current foreground process,
# which by default translates into terminating the application.
# CtrlD tells the terminal that it should register a EOF on standard input,
# which bash interprets as a desire to exit.
# EOF is not a character (in most modern operating systems).
# It is simply a condition that applies to a file stream when the
# end of the stream is reached.
# The confusion arises because a user may signal EOF for console
# input by typing a special character (e.g Control-D in Unix, Linux, et al),
# but this character is not seen by the running program, it is caught by
# the operating system which in turn signals EOF to the process.

    """ if there is no command-line arg, prompt for user input """
    if len(argv[1:]) == 0:
        arg = ''
        while True:
            try:
                arg = input()
            except EOFError:
                # EOF reached with ctrl + D
                # we need to add a space for the carriage return
                carriage_ret = 1
                break
            except KeyboardInterrupt:
                # exception raises when ctrl + C
                break
    else:
        """ catches program last argument """
        arg = argv[-1]

    print("The text contains " + str(len(arg) + carriage_ret) +
          " characters: ")

    """ count occurences of below char ranges """
    i = 0
    for item in arg:
        if item.isupper():
            i += 1
    print(str(i) + " upper letters")
    i = 0
    for item in arg:
        if item.islower():
            i += 1
    print(str(i) + " lower letters")
    i = 0
    for item in arg:
        if item in punctuation:
            i += 1
    print(str(i) + " punctuation marks")
    i = 0
    for item in arg:
        if item in spaces:
            i += 1 + carriage_ret
    print(str(i) + " spaces")
    i = 0
    for item in arg:
        if item.isdigit():
            i += 1
    print(str(i) + " digits")


if __name__ == "__main__":
    main()

# In Python, __name__ is a special variable assigned to the name
# of the Python module by the interpreter. If your module is invoked as
# a script, then the string ‘__main__’ will automatically be assigned
# to the special variable __name__.
# But if you import your module into another module, the string
# ‘my_module’ will be assigned to __name__.
# When a module is invoked as a string, then Python interpreter will
# assign the string '__main__' to a special variable called __name__,
# and the code, which is defined under the condition
# if __name__ == ‘__main__', will subsequently get executed.
# On the other hand, when a module is imported in another module,
# then the Python interpreter will assign the string with the name
# of that module to the special variable __name__. This means that in
# such cases if __name__ == ‘__main__’ will evaluate to False which means that
# only the code outside of this condition will get executed once imported.
