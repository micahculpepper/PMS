import os
import sys
import multiprocessing
import time
import random


def output():
    pid = os.getpid()
    time.sleep(random.random())
    print(f"stdout from pid {pid}")
    print(f"stderr from pid {pid}", file=sys.stderr)


def main(argv):
    n_procs = multiprocessing.cpu_count() * 8
    processes = [multiprocessing.Process(target=output) for _ in range(n_procs)]
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
