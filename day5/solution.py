# ---Hydrothermal Venture---
# https://adventofcode.com/2021/day/5

from pathlib import Path
from collections import defaultdict


def parse_data(line):
    line = [int(a) for a in line.replace(" -> ", ",").split(",")]
    return line


def draw_vents(input_data, ignore_diagonal=True):
    points = defaultdict(int)
    for x1, y1, x2, y2 in input_data:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                points[x1, y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                points[x, y1] += 1
        elif not ignore_diagonal and abs(x1 - x2) == abs(y1 - y2):
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            for n in range(abs(x1 - x2) + 1):
                points[x1 + n * dx, y1 + n * dy] += 1
    return sum(1 for vents in points.values() if vents > 1)


# ========= Part I =========


def part1(data):
    return draw_vents(data)


# ========= Part II =========


def part2(data):
    return draw_vents(data, False)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = list(map(parse_data, open(p).read().splitlines()))
    print(part1(input_data))
    print(part2(input_data))
