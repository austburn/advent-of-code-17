def checksum(code):
    ceiling, floor = int(code[0]), int(code[0])

    for char in code:
        char_int = int(char)
        if char_int < floor:
            floor = char_int
        elif char_int > ceiling:
            ceiling = char_int

    return ceiling - floor
