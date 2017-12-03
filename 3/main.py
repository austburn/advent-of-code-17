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
    x, y = 0, 0
    layer, rng = determine_layer(num)
    idx = rng.index(num)
    nums_per_side = int(len(rng)/4) + 1

    right = rng[0:nums_per_side-1]
    right.append(rng[-1])
    top_right_corner_idx = math.floor(nums_per_side/2)
    top = rng[top_right_corner_idx:top_right_corner_idx+nums_per_side]
    left = rng[top_right_corner_idx+nums_per_side-1:nums_per_side*2]
    bottom = rng[top_right_corner_idx+(nums_per_side*2)-2:]

    if num in right:
        x = layer
    if num in left:
        x = -layer

    if num in top:
        y = layer
    if num in bottom:
        y = -layer

    return x, y


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:')
        print('\tpython main.py 1234')
    else:
        print(determine_layer(int(sys.argv[1])))
