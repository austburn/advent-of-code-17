import sys

NEXT = 'NEXT'
HALF = 'HALF'

def captcha(line, jump_behavior=NEXT):
    captcha_sum = 0
    jump = 0
    if jump_behavior == NEXT:
        jump = 1
    elif jump_behavior == HALF:
        jump = int(len(line)/2)

    for idx, ch in enumerate(line):
        if line[idx] == line[(idx+jump)%len(line)]:
            captcha_sum += int(line[idx])
    return captcha_sum

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            for line in f:
                print('First: %s' % captcha(line.rstrip('\n')))
                print('Second: %s' % captcha(line.rstrip('\n'), jump_behavior=HALF))
