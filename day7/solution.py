# ---The Treachery of Whales---
# https://adventofcode.com/2021/day/7

from pathlib import Path
from collections import defaultdict


def parse_data(line):
    return [int(a) for a in line.split(",")]


# ========= Part I =========


def part1(data):
    fuel_consumption = defaultdict(int)
    for i in range(max(data)):
        fuel_consumption[i] = sum(list(map(lambda x: abs(x - i), data)))
    min_ = min(fuel_consumption, key=fuel_consumption.get)
    return fuel_consumption[min_]


# ========= Part II =========


def part2(data):
    return min(
        [
            sum((abs(t - crab) + 1) * abs(t - crab) // 2 for crab in data)
            for t in range(min(data), max(data) + 1)
        ]
    )


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    crabs = list(map(parse_data, open(p).read().splitlines()))[0]
    print(part1(crabs))
    print(part2(crabs))
