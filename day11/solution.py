# ---Dumbo Octopus---
# https://adventofcode.com/2021/day/11

from itertools import count, product
from pathlib import Path


def parse_data(input_data):
    board = {
        x + 1j * y: int(input_data[x][y]) for (x, y) in product(range(10), repeat=2)
    }
    dirs = {z for (x, y) in product((-1, 0, 1), repeat=2) if (z := x + y * 1j)}
    adjacent = {w: {w + z for z in dirs} & set(board) for w in board}
    return board, adjacent


def step(level, adjacent):
    for w in level:
        level[w] += 1
    flashed = set()
    while True:
        flashing = {w for w, l in level.items() if l > 9} - flashed
        if not flashing:
            for w in flashed:
                level[w] = 0
            return len(flashed)
        flashed |= flashing
        for w in flashing:
            for z in adjacent[w]:
                level[z] += 1


# ========= Part I =========


def part1(board, adjacent):
    level = dict(board)
    return sum(step(level, adjacent) for _ in range(100))


# ========= Part II =========


def part2(board, adjacent):
    level = dict(board)
    return next(i for i in count(1) if step(level, adjacent) == 100)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = p.open().read().strip().split("\n")
    board, adjacent = parse_data(input_data)
    print(part1(board, adjacent))
    print(part2(board, adjacent))
