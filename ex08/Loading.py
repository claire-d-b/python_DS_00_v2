import sys
import os
from datetime import timedelta
from time import sleep, time


def ft_tqdm(items: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.

    Parameters
    ----------
    iterable  : iterable, optional
        Iterable to decorate with a progressbar.
        Leave blank to manually manage the updates.
    desc  : str, optional
        Prefix for the progressbar.
    total  : int or float, optional
        The number of expected iterations. If unspecified,
        len(iterable) is used if possible. If float("inf") or as a last
        resort, only basic progress statistics are displayed
        (no ETA, no progressbar).
        If `gui` is True and this parameter needs subsequent updating,
        specify an initial arbitrary large positive number,
        e.g. 9e9.
    leave  : bool, optional
        If [default: True], keeps all traces of the progressbar
        upon termination of iteration.
        If `None`, will leave only if `position` is `0`.
    file  : `io.TextIOWrapper` or `io.StringIO`, optional
        Specifies where to output the progress messages
        (default: sys.stderr). Uses `file.write(str)` and `file.flush()`
        methods.  For encoding, see `write_bytes`.
    ncols  : int, optional
        The width of the entire output message. If specified,
        dynamically resizes the progressbar to stay within this bound.
        If unspecified, attempts to use environment width. The
        fallback is a meter width of 10 and no limit for the counter and
        statistics. If 0, will not print any meter (only stats).
    mininterval  : float, optional
        Minimum progress display update interval [default: 0.1] seconds.
    maxinterval  : float, optional
        Maximum progress display update interval [default: 10] seconds.
        Automatically adjusts `miniters` to correspond to `mininterval`
        after long display update lag. Only works if `dynamic_miniters`
        or monitor thread is enabled.
    miniters  : int or float, optional
        Minimum progress display update interval, in iterations.
        If 0 and `dynamic_miniters`, will automatically adjust to equal
        `mininterval` (more CPU efficient, good for tight loops).
        If > 0, will skip display of specified number of iterations.
        Tweak this and `mininterval` to get very efficient loops.
        If your progress is erratic with both fast and slow iterations
        (network, skipping items, etc) you should set miniters=1.
    ascii  : bool or str, optional
        If unspecified or False, use unicode (smooth blocks) to fill
        the meter. The fallback is to use ASCII characters " 123456789#".
    disable  : bool, optional
        Whether to disable the entire progressbar wrapper
        [default: False]. If set to None, disable on non-TTY.
    unit  : str, optional
        String that will be used to define the unit of each iteration
        [default: it].
    unit_scale  : bool or int or float, optional
        If 1 or True, the number of iterations will be reduced/scaled
        automatically and a metric prefix following the
        International System of Units standard will be added
        (kilo, mega, etc.) [default: False]. If any other non-zero
        number, will scale `total` and `n`.
    dynamic_ncols  : bool, optional
        If set, constantly alters `ncols` and `nrows` to the
        environment (allowing for window resizes) [default: False].
    smoothing  : float, optional
        Exponential moving average smoothing factor for speed estimates
        (ignored in GUI mode). Ranges from 0 (average speed) to 1
        (current/instantaneous speed) [default: 0.3].
    bar_format  : str, optional
        Specify a custom bar string formatting. May impact performance.
        [default: '{l_bar}{bar}{r_bar}'], where
        l_bar='{desc}: {percentage:3.0f}%|' and
        r_bar='| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, '
            '{rate_fmt}{postfix}]'
        Possible vars: l_bar, bar, r_bar, n, n_fmt, total, total_fmt,
            percentage, elapsed, elapsed_s, ncols, nrows, desc, unit,
            rate, rate_fmt, rate_noinv, rate_noinv_fmt,
            rate_inv, rate_inv_fmt, postfix, unit_divisor,
            remaining, remaining_s, eta.
        Note that a trailing ": " is automatically removed after {desc}
        if the latter is empty.
    initial  : int or float, optional
        The initial counter value. Useful when restarting a progress
        bar [default: 0]. If using float, consider specifying `{n:.3f}`
        or similar in `bar_format`, or specifying `unit_scale`.
    position  : int, optional
        Specify the line offset to print this bar (starting from 0)
        Automatic if unspecified.
        Useful to manage multiple bars at once (eg, from threads).
    postfix  : dict or *, optional
        Specify additional stats to display at the end of the bar.
        Calls `set_postfix(**postfix)` if possible (dict).
    unit_divisor  : float, optional
        [default: 1000], ignored unless `unit_scale` is True.
    write_bytes  : bool, optional
        Whether to write bytes. If (default: False) will write unicode.
    lock_args  : tuple, optional
        Passed to `refresh` for intermediate output
        (initialisation, iterating, and updating).
    nrows  : int, optional
        The screen height. If specified, hides nested bars outside this
        bound. If unspecified, attempts to use environment height.
        The fallback is 20.
    colour  : str, optional
        Bar colour (e.g. 'green', '#00ff00').
    delay  : float, optional
        Don't display until [default: 0] seconds have elapsed.
    gui  : bool, optional
        WARNING: internal parameter - do not use.
        Use tqdm.gui.tqdm(...) instead. If set, will attempt to use
        matplotlib animations for a graphical output [default: False].

    Returns
    -------
    out  : decorated iterator."""
    # Yield is used in a function to make it a generator.
    # Instead of returning a value and ending the function,
    # yield produces a value and pauses the function, saving its state
    # for future use.
    # - yield turns a function into a generator.
    # - It pauses the function and returns a value each time it’s called.
    # - The function’s state is saved between calls.
    # - Useful for memory-efficient, stateful iteration over large
    # or infinite sequences. Here we 100 as a base."""
    size = os.get_terminal_size()
    cols = (size[0] - 5 - 38)
    progress = 0
    timestamp = 0
    start = time()
    if len(list(items)):
        to_print = ""
        for i in range(0, len(list(items))):
            progress = int(i * cols / 333)
            nstring = to_print.replace(to_print,
                                       str(round(i * 100 / 333))+"%|")
            sys.stdout.flush()  # Ensures the output is flushed
            # (especially important for buffered I/O)
            to_print_bar = "█"
            if i == (len(list(items)) - 1):
                print(f"{to_print_bar * (progress + 1)}", end="")
                sys.stdout.flush()
                print(f"| {len(list(items))}/{len(list(items))} ", end="")
                sys.stdout.flush()

                end = time()
                timestamp = end - start
                print("[" + str(timedelta(seconds=round(timestamp))) + "<" +
                      str(timedelta(microseconds=(timestamp - round(timestamp
                                                                    ))))
                      + ", " + str(round(len(list(items)) / timestamp, 2)) +
                      "it/s]", end="\r")
                sys.stdout.flush()
            else:
                print(f"{to_print_bar * progress}", end='\r')
            if round(i * cols / 333) % 10 == 0:
                sleep(0.05)
            sys.stdout.flush()
            print(f"{nstring}", end="")
            sys.stdout.flush()

        yield progress
        # a return here would raise a TypeError: 'int' object is not iterable
        # Actually : return: It immediately exits the function and sends back
        # a value to the caller.
        # Once return is used, the function stops running.
        # yield: It pauses the function and sends a value to the caller,
        # but the function's state is saved.
        # chatgpt example :
        # def my_generator():
        #     yield 1
        #     yield 2
        #     yield 3

        # for value in my_generator():
        #     print(value)  -> prints 1, 2, 3 one by one
