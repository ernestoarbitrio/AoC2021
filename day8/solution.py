# ---Seven Segment Search---
# https://adventofcode.com/2021/day/8

from pathlib import Path
import functools
import operator


def parse_data(data):
    patterns = [a.split("|")[0].strip().split() for a in data.splitlines()]
    outputs = [a.split("|")[1].strip().split() for a in data.splitlines()]
    return patterns, outputs


def mapping(patterns):
    pattern_to_digit = {}

    for p, plen in patterns:
        if plen == 2:
            pattern_to_digit[p] = 1
        elif plen == 3:
            pattern_to_digit[p] = 7
        elif plen == 4:
            pattern_to_digit[p] = 4
        elif plen == 7:
            pattern_to_digit[p] = 8

    digit_to_pattern = {v: k for k, v in pattern_to_digit.items()}

    for p, plen in patterns:
        if p in pattern_to_digit:
            continue

        if plen == 5:
            if len(p & digit_to_pattern[1]) == 2:
                pattern_to_digit[p] = 3
            elif len(p & digit_to_pattern[4]) == 3:
                pattern_to_digit[p] = 5
            else:
                pattern_to_digit[p] = 2
        else:
            if len(p & digit_to_pattern[4]) == 4:
                pattern_to_digit[p] = 9
            elif len(p & digit_to_pattern[7]) == 2:
                pattern_to_digit[p] = 6
            else:
                pattern_to_digit[p] = 0

    return pattern_to_digit


# ========= Part I =========


def part1(data):
    count_ = list(map(lambda x: [1 for e in x if len(e) in (2, 3, 4, 7)], data))
    return len(functools.reduce(operator.iconcat, count_, []))


# ========= Part II =========


def part2(data):
    total = 0
    for line in data.splitlines():
        patterns, digits = map(str.split, line.split("|"))
        patterns = tuple(map(lambda p: (frozenset(p), len(p)), patterns))
        digits = tuple(map(lambda p: (frozenset(p), len(p)), digits))
        maps = mapping(patterns)
        total += maps[digits[0][0]] * 1000
        total += maps[digits[1][0]] * 100
        total += maps[digits[2][0]] * 10
        total += maps[digits[3][0]]
    return total


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    patterns, outputs = parse_data(open(p).read())
    print(part1(outputs))
    print(part2(open(p).read()))
