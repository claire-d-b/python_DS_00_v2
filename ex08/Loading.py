import sys
import time
from datetime import datetime

def generator(items: range):
    for i in items:
        print('█', sep=None, end="")
        yield i
from time import sleep

def ft_tqdm(items: range) -> None:
    """ yield is used in a function to make it a generator.
    Instead of returning a value and ending the function,
    yield produces a value and pauses the function, saving its state
    for future use.
    - yield turns a function into a generator.
    - It pauses the function and returns a value each time it’s called.
    - The function’s state is saved between calls.
    - Useful for memory-efficient, stateful iteration over large
    or infinite sequences. """
    progress = 0
    # to_print = ""
    start = datetime.now()
    if len(list(items)):
        max = 113
        to_print = ""
        for i in range(0, len(list(items))):
            # nonlocal progress
            progress = int(i * 113 / 333)
            # nonlocal to_print
            if (round(i * 100 / 333)) % 100 == 0:
                nstring = to_print.replace(to_print, str(round(i * 100 / 333))+"%|")
            elif round(i * 100 / 333) % 10 == 0:
                nstring = to_print.replace(to_print, ' '+str(round(i * 100 / 333))+"%|")
            else:
                nstring = to_print.replace(to_print, '  '+str(round(i * 100 / 333))+"%|")
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)


            # print("prog", int(progress * 100 / 113))
            # sys.stdout.write("█" * progress)
            # progress_bar = '=' * int(self.ncols * (self.n / self.total))

            # print(nstring, end="")
            # sys.stdout.write(f"{nstring}")
            to_print_bar = "█"
            if i == (len(list(items)) - 1):
                print(f"     {to_print_bar * (progress + 1)}", end="")
                print(f"| {len(list(items))}/{len(list(items))}", end='\r')
                sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)
            else:
                print(f"     {to_print_bar * progress}", end='\r')
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)
            sleep(0.005)
            print(f"{nstring}", end='\r')
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)



            # sys.stdout.flush(False)
            if (i == len(list(items)) - 1):
                for x in range (0, progress):
                    if x % 10:
                        sleep(0.005)
            # return (progress, to_print)
            # print(to_print)

        # ntuple = inner()
        # progress, to_print = ntuple[0], ntuple[1]
        if (i == len(list(items))):
            print(f"| {len(list(items))}/{len(list(items))} []")
        end = datetime.now()
        timestamp = (end - start)
        timestamp.strftime("%M:%S")
        print(timestamp)
        # print(f"|{len(list(items))}/{len(list(items))}")
        yield progress
    # The flush() method ensures that the data is immediately written to the output buffer rather than
    # waiting for the buffer to fill.
# print("█" * len(list(items), end="")
#     maxv = max(list(items))
#     print(maxv)
#     for i in range(0, maxv):
#         i = int(i * 113 / 333)
#         yield i

    # i = 0
    # print("100%|", end="")
    # x = 0
    # maxv = max(list(items))
    # if i == maxv:
    #     print(f"{len(items)}/{len(items)}")
    # return generator
    # iterable, total or nb of expected iterations,
    # leave : [default: True], keeps all traces of the
    # progressbar upon termination of iteration. If None,
    # will leave only if position is 0.
    # unit=it by default
# 113 chars