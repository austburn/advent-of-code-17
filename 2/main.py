def checksum(code):
    min_ceiling = 0
    max_floor = 9

    for char in code:
        char_int = int(char)
        if char_int < max_floor:
            max_floor = char_int
        elif char_int > min_ceiling:
            min_ceiling = char_int

    return min_ceiling - max_floor
