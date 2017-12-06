import sys


def determine_maze_exit(maze):
    return -1


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            maze = [line.rstrip('\n') for line in f.readlines()]
            print(determine_maze_exit(maze))
