# ---Dive!---
# https://adventofcode.com/2021/day/2

from functools import reduce
from pathlib import Path


def parse_entry(s):
    s = s.split()
    selector = {
        "forward": (int(s[1]), 0),
        "up": (0, -int(s[1])),
        "down": (0, int(s[1])),
    }
    return selector.get(s[0])


# ========= Part I =========


def part1(input_data):
    h_position, depth = [sum(d) for d in zip(*input_data)]
    return h_position * depth


# ========= Part II =========


def part2(input_data):
    def tune_position(pos, data):
        if data[1] == 0:
            return (pos[0] + data[0], pos[1] + data[0] * pos[2], pos[2])
        else:
            return (pos[0], pos[1], pos[2] + data[1])

    h_position, depth, _ = reduce(tune_position, input_data, (0, 0, 0))
    return h_position * depth


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = list(map(parse_entry, open(p).read().splitlines()))
    print(part1(input_data))
    print(part2(input_data))
