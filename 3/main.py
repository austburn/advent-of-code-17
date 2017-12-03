def determine_layer(num):
    return num


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py 1234')
    else:
        print(determine_layer(int(sys.argv[1])))
