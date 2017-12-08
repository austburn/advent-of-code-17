import sys
import re
# pbga (66)
# xhth (57)
# ebii (61)
# havc (66)
# ktlj (57)
# fwft (72) -> ktlj, cntj, xhth
def parse_program(program):
    rgx = re.compile('(?P<name>\w+) \((?P<weight>\d+)\)( -> (?P<programs>(\w+(, )?)+))?')
    program_dict = rgx.match(program).groupdict()
    if program_dict['programs'] is not None:
        program_dict['programs'] = [p.strip() for p in program_dict['programs'].split(',')]
    return program_dict


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print('yay')
