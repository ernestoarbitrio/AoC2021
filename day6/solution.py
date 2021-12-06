# ---Lanternfish---
# https://adventofcode.com/2021/day/6

from pathlib import Path
from collections import defaultdict


def parse_data(line):
    return [int(a) for a in line.split(",")]


def fish_counter_per_day(data, days=80):
    timers = defaultdict(int)
    for fish in data[0]:
        timers[fish] += 1

    for _ in range(days):
        day_0_fish = timers[0]
        for i in range(8):
            timers[i] = timers[i + 1]
        timers[6] += day_0_fish
        timers[8] = day_0_fish

    return sum(timers.values())


# ========= Part I =========


def part1(data):
    return fish_counter_per_day(data)


# ========= Part II =========


def part2(data, days):
    return fish_counter_per_day(data, days)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = list(map(parse_data, open(p).read().splitlines()))
    print(part1(input_data))
    print(part2(input_data, 256))
