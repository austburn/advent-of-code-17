import sys
import re


def is_group(input):
    rgx = re.compile('\{.*\}')
    return bool(rgx.match(input))

def is_trash(input):
    rgx = re.compile('\<.*\>')
    return bool(rgx.match(input))

def remove_voids(input):
    return input.replace('!!', '').replace('!>', '').replace('!<', '')

def _parse_groups_and_trash(input, group_value=1):
    import pdb;pdb.set_trace()
    if input == '':
        return 0
    if is_trash(input):
        return 0
    if is_group(input):
        innards = input[1:len(input)-1]
        if is_trash(innards):
            return group_value
        return group_value + sum([_parse_groups_and_trash(c, group_value=group_value+1) for c in innards.split(',')])

    return group_value

def traverse_groups(input):
    sanitized = remove_voids(input)
    return _parse_groups_and_trash(sanitized)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print()
