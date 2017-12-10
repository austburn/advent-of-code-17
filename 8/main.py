import sys
import re


OPERATIONS = {
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '==': lambda x, y: x == y,
    '!=': lambda x, y: x != y,
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}


def parse_instruction(instruction):
    rgx = re.compile('(?P<register>\w+) (?P<operation>(inc|dec)) (?P<value>\-?\d+) if (?P<condition_register>\w+) (?P<condition_operator>[<>!=]+) (?P<condition_value>\-?\d+)')
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


def run_instruction_set(instructions):
    registers = {}
    max_value = ('', 0)
    for instruction in instructions:
        parsed_instruction = parse_instruction(instruction)
        dest_reg = parsed_instruction['register']
        op_reg = parsed_instruction['condition']['register']
        if dest_reg not in registers:
            registers[dest_reg] = 0
        if op_reg not in registers:
            registers[op_reg] = 0
        if OPERATIONS[parsed_instruction['condition']['operation']](registers[op_reg], parsed_instruction['condition']['value']):
            registers[dest_reg] = OPERATIONS[parsed_instruction['operation']](registers[dest_reg], parsed_instruction['value'])
            if registers[dest_reg] > max_value[1]:
                max_value = (dest_reg, registers[dest_reg])
    return max(registers.items(), key=lambda x: x[1]), max_value

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print(run_instruction_set([f.rstrip('\n') for f in f.readlines()]))
