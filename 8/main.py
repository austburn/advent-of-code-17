import sys
import re


def parse_instruction(instruction):
    rgx = re.compile('(?P<register>\w) (?P<operation>(inc|dec)) (?P<value>\d) if (?P<condition_register>\w) (?P<condition_operator>[<>!=]+) (?P<condition_value>\d)')
    match_dict = rgx.match(instruction).groupdict()
    return {
        'register': match_dict['register'],
        'operation': match_dict['operation'],
        'value': int(match_dict['value']),
        'condition': {
            'register': match_dict['condition_register'],
            'operation': match_dict['condition_operator'],
            'value': int(match_dict['condition_value'])
        }
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print('')
