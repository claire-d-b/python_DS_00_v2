import sys
import time
from datetime import datetime, timedelta

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
    timestamp = 0
    start = time.time()
    if len(list(items)):
        max = 100
        to_print = ""
        for i in range(0, len(list(items))):
            # nonlocal progress
            progress = int(i * 100 / 333)
            # nonlocal to_print
            nstring = to_print.replace(to_print, str(round(i * 100 / 333))+"%|")
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)


            # print("prog", int(progress * 100 / 100))
            # sys.stdout.write("█" * progress)
            # progress_bar = '=' * int(self.ncols * (self.n / self.total))

            # print(nstring, end="")
            # sys.stdout.write(f"{nstring}")
            to_print_bar = "█"
            if i == (len(list(items)) - 1):
                print(f"{to_print_bar * (progress + 1)}", end="")
                print(f"| {len(list(items))}/{len(list(items))}", end="")
                end = time.time()
                timestamp = end - start
                print("["+str(timedelta(seconds=round(timestamp)))+"<"+str(timedelta(microseconds=(timestamp - round(timestamp))))+", "+str(round(333 / float(timestamp), 2))+"it/s]", end="\r")
                sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)
            else:
                print(f"{to_print_bar * progress}", end='\r')
            if round(i * 100 / 333) % 10 == 0:
                sleep(0.05)
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)
            print(f"{nstring}", end="")
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)

            # sys.stdout.flush(False)
            # if (i == len(list(items)) - 1):
            #     for x in range (0, progress):
            #         if x % 10 == 0:
            #             sleep(0.1)
            # return (progress, to_print)
            # print(to_print)

        # ntuple = inner()
        # progress, to_print = ntuple[0], ntuple[1]
            # print(f"| {len(list(items))}/{len(list(items))} []")

        # str(datetime.timedelta(seconds=timestamp))
        # print(f"|{len(list(items))}/{len(list(items))}")
        yield progress
    # The flush() method ensures that the data is immediately written to the output buffer rather than
    # waiting for the buffer to fill.
# print("█" * len(list(items), end="")
#     maxv = max(list(items))
#     print(maxv)
#     for i in range(0, maxv):
#         i = int(i * 100 / 333)
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
# 100 chars