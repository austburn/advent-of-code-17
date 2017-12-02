import sys


def captcha(line):
    captcha_sum = 0
    for idx, ch in enumerate(line):
        if idx+1 < len(line) and line[idx] == line[idx+1]:
            captcha_sum += int(line[idx])

    if len(line) > 1 and line[0] == line[-1]:
        captcha_sum += int(line[0])
    return captcha_sum

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            for line in f:
                print(captcha(line.rstrip('\n')))
