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
    else:
        program_dict['programs'] = []
    return program_dict


def _determine_chain_length(name, programs, depth=0):
    next_layer_programs = programs[name]['programs']
    if len(next_layer_programs) == 0:
        return depth
    else:
        return max([_determine_chain_length(n, programs, depth=depth+1) for n in next_layer_programs])


def determine_tree_root(program_map):
    lengths = []
    for name, program in program_map.items():
        lengths.append((name, _determine_chain_length(name, program_map)))

    return max(lengths, key=lambda x: x[1])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            programs = [parse_program(p.rstrip('\n')) for p in f.readlines()]
            program_map = {p['name']: p for p in programs}

            print(determine_tree_root(program_map))
