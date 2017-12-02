import sys


def line_checksum(line):
    ceiling, floor = int(line[0]), int(line[0])

    for char in line:
        char_int = int(char)
        if char_int < floor:
            floor = char_int
        elif char_int > ceiling:
            ceiling = char_int

    return ceiling - floor


def file_checksum(lines):
    file_sum = 0
    for line in lines:
        full_line = line.split()
        file_sum += line_checksum(full_line)
    return file_sum


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print(file_checksum(f.readlines()))
