import sys
import copy


def realloc_memory(cores):
    max_blocks = max(cores)
    start_idx = cores.index(max_blocks)
    cores[start_idx] = 0
    for x in range(max_blocks):
        cores[(start_idx+x+1)%len(cores)] += 1
    return cores

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            cores = [int(val) for val in f.readlines()[0].split()]
            print(cores)
            print(realloc_memory(cores))
