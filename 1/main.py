import sys


def captcha(line):
    return int(line[0])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            for line in f:
                print(captcha(line))
