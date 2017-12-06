import sys


def anagram(a, b):
    if len(a) != len(b):
        return False

    matches = 0
    for letter in a:
        try:
            b.index(letter)
        except ValueError:
            return False
        else:
            matches += 1

    return matches == len(a)


def has_anagrams(phrase):
    for i, p in enumerate(phrase):
        for x in range(len(phrase)-1, i, -1):
            if anagram(p, phrase[x]):
                return True
    return False



def valid_passcodes(codes):
    num_valid_passcodes = 0
    for code in codes:
        phrase = code.split()
        phrase_set = set(phrase)
        if len(phrase) == len(phrase_set):
            if not has_anagrams(phrase):
                num_valid_passcodes += 1

    return num_valid_passcodes


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython anagrams.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            print(valid_passcodes(f.readlines()))
