# ---Smoke Basin---
# https://adventofcode.com/2021/day/9

from pathlib import Path
from math import prod


def parse_data(line):
    return [int(x) for x in line.strip()]


def find_adjacents(data, x, y):
    output = []
    if x > 0:
        output.append((x - 1, y))
    if x < len(data[y]) - 1:
        output.append((x + 1, y))
    if y > 0:
        output.append((x, y - 1))
    if y < len(data) - 1:
        output.append((x, y + 1))
    return output


def basins_len(data):
    basin_lenghts = []
    width, height = len(data[0]), len(data)
    visited = set()

    def _get_basin_length(y: int, x: int):
        if (y, x) in visited or data[y][x] == 9:
            return 0
        visited.add((y, x))
        basin_legth = 1
        # right
        if x < len(data[0]) - 1:
            basin_legth += _get_basin_length(y, x + 1)
        # down
        if y < len(data) - 1:
            basin_legth += _get_basin_length(y + 1, x)
        # left
        if x:
            basin_legth += _get_basin_length(y, x - 1)
        # up
        if y:
            basin_legth += _get_basin_length(y - 1, x)
        return basin_legth

    basin_lenghts = [
        _get_basin_length(y, x) for y in range(height) for x in range(width)
    ]

    return prod(sorted(basin_lenghts, reverse=True)[:3])


# ========= Part I =========


def part1(data):
    low_points = []
    for y, row in enumerate(data):
        for x, location in enumerate(row):
            if all(
                data[other[1]][other[0]] > location
                for other in find_adjacents(data, x, y)
            ):
                low_points.append((x, y))
    return sum(data[coords[1]][coords[0]] + 1 for coords in low_points)


# ========= Part II =========


def part2(data):
    return basins_len(data)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input = list(map(parse_data, open(p).read().splitlines()))
    print(part1(input))
    print(part2(input))
