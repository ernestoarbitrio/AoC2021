# ---Dive!---
# https://adventofcode.com/2021/day/2

from functools import reduce

# ========= Data =========


def parse_entry(s):
    s = s.split()
    selector = {
        "forward": (int(s[1]), 0),
        "up": (0, -int(s[1])),
        "down": (0, int(s[1])),
    }
    return selector.get(s[0])


input_data = list(map(parse_entry, open("input.txt").read().splitlines()))

# ========= Part I =========
horizontal_position, depth = [sum(d) for d in zip(*input_data)]

print(horizontal_position * depth)


# ========= Part II =========


def tune_position(pos, data):
    if data[1] == 0:
        return (pos[0] + data[0], pos[1] + data[0] * pos[2], pos[2])
    else:
        return (pos[0], pos[1], pos[2] + data[1])


horizontal_position, depth, _ = reduce(tune_position, input_data, (0, 0, 0))

print(horizontal_position * depth)
