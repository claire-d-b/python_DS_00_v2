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
    or infinite sequences. Here we 100 as a base."""
    progress = 0
    timestamp = 0
    start = time.time()
    if len(list(items)):
        max = 100
        to_print = ""
        for i in range(0, len(list(items))):
            progress = int(i * 100 / 333)
            nstring = to_print.replace(to_print, str(round(i * 100 / 333))+"%|")
            sys.stdout.flush()  # Ensures the output is flushed (especially important for buffered I/O)
            to_print_bar = "█"
            if i == (len(list(items)) - 1):
                print(f"{to_print_bar * (progress + 1)}", end="")
                sys.stdout.flush()

                print(f"| {len(list(items))}/{len(list(items))}", end="")
                sys.stdout.flush()

                end = time.time()
                timestamp = end - start
                print("["+str(timedelta(seconds=round(timestamp)))+"<"+str(timedelta(microseconds=(timestamp - round(timestamp))))+", "+str(round(333 / float(timestamp), 2))+"it/s]", end="\r")
                sys.stdout.flush()
            else:
                print(f"{to_print_bar * progress}", end='\r')
            if round(i * 100 / 333) % 10 == 0:
                sleep(0.05)
            sys.stdout.flush()
            print(f"{nstring}", end="")
            sys.stdout.flush()

        yield progress