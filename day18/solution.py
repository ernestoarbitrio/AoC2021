# ---Snailfish---
# https://adventofcode.com/2021/day/18


from functools import reduce
import math
from pathlib import Path


def parse_data(data):
    sections = data.rstrip().split("\n")
    return [eval(section) for section in sections]


def add_right(s, n):
    if isinstance(s, int):
        return s + n
    return [s[0], add_right(s[1], n)]


def add_left(s, n):
    if isinstance(s, int):
        return s + n
    return [add_left(s[0], n), s[1]]


def explode(snail, depth=0):
    if isinstance(snail, int):
        return snail, False, 0, 0
    if depth == 4:
        return 0, True, snail[0], snail[1]
    left, exploded, sum_left, sum_right = explode(snail[0], depth + 1)
    if exploded:
        return [left, add_left(snail[1], sum_right)], True, sum_left, 0
    right, exploded, sum_left, sum_right = explode(snail[1], depth + 1)
    if exploded:
        return [add_right(snail[0], sum_left), right], True, 0, sum_right
    return [left, right], False, 0, 0


def sum_snails(s, r):
    def split(s):
        if isinstance(s, int):
            return (s, False) if s < 10 else ([s // 2, math.ceil(s / 2)], True)
        left, splitted = split(s[0])
        if splitted:
            return [left, s[1]], True
        right, splitted = split(s[1])
        return [left, right], splitted

    def reduce_snails(s):
        s, exploded, _, _ = explode(s)
        if exploded:
            return reduce_snails(s)
        s, splitted = split(s)
        if splitted:
            return reduce_snails(s)
        return s

    return reduce_snails([s, r])


def magnitude(s):
    if isinstance(s, int):
        return s
    return (3 * magnitude(s[0])) + (2 * magnitude(s[1]))


def part1(snails):
    return magnitude(reduce(sum_snails, snails[1:], snails[0]))


def part2(snails):
    return max(magnitude(sum_snails(sa, sb)) for sa in snails for sb in snails)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = parse_data(open(p).read())
    print(part1(input_data))
    print(part2(input_data))
