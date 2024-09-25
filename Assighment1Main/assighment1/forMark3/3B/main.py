import time
import os
from sunday import binary_sunday_search as sunday
from rabin_karp_search import rabin_karp_search as rabin_karp
from z_algorithm import gusfield_z_search as gusfield_z

import matplotlib.pyplot as plt

TIMES = 100

def timeit(pat, txt, func):
    start_time = time.time()
    func(txt, pat)
    end_time = time.time()
    return (end_time - start_time) * 1e6  # convert to microseconds

def read_file_as_string(file_path):
    if not os.path.isfile(file_path):
        raise RuntimeError(f"Failed to open file {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def main():
    # Case 1: Binary Sunday (the first algorithm covered in class) is at least twice as fast as Gusfield Z.
    text1 = read_file_as_string("text1.txt")
    pattern1 = read_file_as_string("pattern1.txt")

    sunday_time = sum(timeit(pattern1, text1, sunday) for _ in range(TIMES)) / TIMES
    gusfield_z_time = sum(timeit(pattern1, text1, gusfield_z) for _ in range(TIMES)) / TIMES

    print(f"Sunday: {sunday_time} microseconds, Gusfield Z: {gusfield_z_time} microseconds")

    

    # Case 3: Rabin-Karp is at least twice as fast as Sunday.
    text3 = read_file_as_string("text3.txt")
    pattern3 = read_file_as_string("pattern3.txt")

    rabin_karp_time_3 = sum(timeit(pattern3, text3, rabin_karp) for _ in range(TIMES)) / TIMES
    sunday_time_3 = sum(timeit(pattern3, text3, sunday) for _ in range(TIMES)) / TIMES

    print(f"Rabin Karp: {rabin_karp_time_3} microseconds, Sunday: {sunday_time_3} microseconds")

    
if __name__ == "__main__":
    main()
