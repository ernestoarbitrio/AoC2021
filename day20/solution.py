# ---Trench Map---
# https://adventofcode.com/2021/day/20

from collections import defaultdict
from itertools import product
from pathlib import Path


grid_relative_indices = list(product((-1, 0, 1), repeat=2))


def find_adj_grid(G):
    return {(x + dx, y + dy) for x, y in G for dy, dx in grid_relative_indices}


def solve(g, rules, iterations):
    new_g = None
    for k in range(iterations):
        new_g = defaultdict(bool)
        adj_grid = find_adj_grid(g)
        for i, j in adj_grid:
            bin_str = ""
            for dx, dy in grid_relative_indices:
                bin_str += str(
                    g.get((i + dx, j + dy), "01"[k % 2] if rules[0] == "#" else "0")
                )
            new_g[(i, j)] = int(rules[int(bin_str, 2)] == "#")
        g = new_g
    return new_g


def parse_data(data):
    rules, input_image = data.split("\n\n")
    data = {
        (i, j): int(v == "#")
        for i, l in enumerate(input_image.split("\n"))
        for j, v in enumerate(l)
    }
    return data, rules


# ========= Part I =========


def part1(data, rules):
    return sum(solve(data, rules, 2).values())


# ========= Part II =========


def part2(data, rules):
    return sum(solve(data, rules, 50).values())


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    data, rules = parse_data(open(p).read())
    print(part1(data, rules))
    print(part2(data, rules))
