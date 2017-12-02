import sys


def line_checksum_min_max(line):
    ceiling, floor = int(line[0]), int(line[0])

    for char in line:
        char_int = int(char)
        if char_int < floor:
            floor = char_int
        elif char_int > ceiling:
            ceiling = char_int

    return ceiling - floor


def line_checksum_division(line):
    for idx, ch in enumerate(line):
        ch_int = int(ch)
        for j in range(len(line)):
            j_int = int(line[j])
            if idx != j:
                if ch_int % j_int == 0:
                    return ch_int/j_int
                elif j_int % ch_int == 0:
                    return j_int/ch_int


def file_checksum(lines, checksum_func=line_checksum_min_max):
    file_sum = 0
    for line in lines:
        full_line = line.split()
        file_sum += checksum_func(full_line)
    return file_sum


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            lines = f.readlines()
            print(file_checksum(lines))
            print(file_checksum(lines, checksum_func=line_checksum_division))
