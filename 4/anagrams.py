import sys


def valid_passcodes(codes):
    num_valid_passcodes = 0
    for code in codes:
        phrase = code.split()
        phrase_set = set(phrase)
        if len(phrase) == len(phrase_set):
            num_valid_passcodes += 1

    return num_valid_passcodes


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython anagrams.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print(valid_passcodes(f.readlines()))
