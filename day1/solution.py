# ---Sonar Sweep---
# https://adventofcode.com/2021/day/1

from itertools import starmap
from operator import lt
from pathlib import Path


# ========= Part I =========


def part1(data):
    couples = zip(data, data[1:])
    return sum(list(starmap(lt, couples)))


# ========= Part II =========


def part2(data):
    windows = zip(data, data[1:], data[2:])
    ws = list(map(sum, windows))
    return sum(list(starmap(lt, zip(ws, ws[1:]))))


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = list(map(int, open(p).read().splitlines()))
    print(part1(input_data))
    print(part2(input_data))
