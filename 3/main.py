import sys
import math

# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25
# layer 1 - 1
#       2 - 8
#       3 - 16
# So... given layer n, n+1 has:
#   nums/side * 4
#   + 4 (additional corners)
def determine_layer(num):
    layer_range = [1]
    current_layer = 0
    while num not in layer_range:
        nums_per_side = int(len(layer_range)/4) + 1
        nums_in_next_layer = (nums_per_side * 4) + 4
        # add one as stop is not included in range
        layer_range = range(layer_range[-1] + 1, layer_range[-1] + nums_in_next_layer + 1)
        current_layer += 1
    return current_layer, list(layer_range)


def determine_coordinates(num):
    layer, rng = determine_layer(num)
    x, y = 0, 0
    nums_per_side = int(len(rng)/4) + 1

    right = rng[0:nums_per_side-1]
    right.append(rng[-1])
    top_right_corner_idx = nums_per_side - 2
    top = rng[top_right_corner_idx:top_right_corner_idx+nums_per_side]
    left = rng[top_right_corner_idx+nums_per_side-1:top_right_corner_idx+(nums_per_side*2)]
    bottom = rng[top_right_corner_idx+(nums_per_side*2)-2:]

    if num in right:
        x = layer
        y = -(layer-1) + right.index(num)
    if num in left:
        x = -layer
        y = layer - left.index(num)
    if num in top:
        x = layer - top.index(num)
        y = layer
    if num in bottom:
        x = -layer + bottom.index(num)
        y = -layer

    return x, y


def taxicab_distance(num):
    dest_x, dest_y = determine_coordinates(num)
    return math.fabs(dest_x) + math.fabs(dest_y)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py 1234')
    else:
        print(taxicab_distance(int(sys.argv[1])))
