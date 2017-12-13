import sys
import re


def traverse_groups(input):
    garbage = False
    i = 0
    group_sum = 0
    group_val = 0
    while i < len(input):
        c = input[i]
        if c == '!':
            i += 2
            continue

        if c == '<':
            garbage = True
        elif c == '>':
            garbage = False
        elif c == '{' and not garbage:
            group_val += 1
            group_sum += group_val
        elif c == '}' and not garbage:
            group_val -= 1

        i += 1
    return group_sum

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print(traverse_groups(f.readlines()[0].rstrip('\n')))
