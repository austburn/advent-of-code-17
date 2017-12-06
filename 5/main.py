import sys


def determine_maze_exit(maze):
    current_index = 0
    num_steps = 0

    while True:
        try:
            steps = maze[current_index]
        except IndexError:
            break
        maze[current_index] = steps + 1
        current_index = current_index + steps
        num_steps += 1

    return num_steps


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py input.txt')
    else:
        with open(sys.argv[1]) as f:
            maze = [int(line.rstrip('\n')) for line in f.readlines()]
            print(determine_maze_exit(maze))
