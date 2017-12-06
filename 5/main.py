import sys
import copy


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


def determine_maze_exit_alternate(maze):
    current_index = 0
    num_steps = 0

    while True:
        try:
            steps = maze[current_index]
        except IndexError:
            break

        if steps >= 3:
            maze[current_index] = steps - 1
        else:
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
            maze_dupe = copy.copy(maze)
            print(determine_maze_exit(maze))
            print(determine_maze_exit_alternate(maze_dupe))
