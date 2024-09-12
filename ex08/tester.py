from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()
    for elem in tqdm(range(333)):
        sleep(0.005)
    print()
    # print(ft_tqdm.__doc__)
    # print(tqdm.__doc__)


if __name__ == "__main__":
    main()

# 100%|██████████| 100/100 [00:10<00:00,  9.90it/s]

# 100%: The loop is fully completed.
# 100/100: Indicates 100 iterations were processed
# out of 100 total.
# 00:10: Elapsed time of 10 seconds.
# 9.90it/s: The speed of processing, showing approximately
# 9.90 iterations per second.

# Calculate total time elapsed and iterations per second
# elapsed_time = end_time - start_time
# iterations = 100 for a range(100)
# iterations_per_second = iterations / elapsed_time
