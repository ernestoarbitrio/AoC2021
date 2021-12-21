# ---Beacon Scanner---
# https://adventofcode.com/2021/day/19

from itertools import combinations
from collections import deque
from pathlib import Path

ORIENTATIONS = [
    (1, 1, 1, 0, 1, 2),
    (1, 1, 1, 1, 2, 0),
    (1, 1, 1, 2, 0, 1),
    (1, 1, -1, 2, 1, 0),
    (1, 1, -1, 1, 0, 2),
    (1, 1, -1, 0, 2, 1),
    (1, -1, -1, 0, 1, 2),
    (1, -1, -1, 1, 2, 0),
    (1, -1, -1, 2, 0, 1),
    (1, -1, 1, 2, 1, 0),
    (1, -1, 1, 1, 0, 2),
    (1, -1, 1, 0, 2, 1),
    (-1, 1, -1, 0, 1, 2),
    (-1, 1, -1, 1, 2, 0),
    (-1, 1, -1, 2, 0, 1),
    (-1, 1, 1, 2, 1, 0),
    (-1, 1, 1, 1, 0, 2),
    (-1, 1, 1, 0, 2, 1),
    (-1, -1, 1, 0, 1, 2),
    (-1, -1, 1, 1, 2, 0),
    (-1, -1, 1, 2, 0, 1),
    (-1, -1, -1, 2, 1, 0),
    (-1, -1, -1, 1, 0, 2),
    (-1, -1, -1, 0, 2, 1),
]


def parse_data(data):
    return [
        {eval(line) for line in scanner.splitlines() if "--" not in line}
        for scanner in data.split("\n\n")
    ]


def scanit(scan, rebased0):
    for rot, rot_scan in rotations(scan).items():
        rebased = {p1: {psub(p1, p2) for p2 in rot_scan} for p1 in rot_scan}
        for p1, p2 in [(p1, p2) for p1 in rebased0 for p2 in rebased]:
            if len(rebased0[p1] & rebased[p2]) > 11:
                return p1, p2, rot


def make_absolute(scanners):
    scanner_locs = {(0, 0, 0)}
    task_list = deque([*enumerate(scanners[1:], start=1)])
    while task_list:
        i, scan = task_list.popleft()
        rebased0 = {p1: {psub(p1, p2) for p2 in scanners[0]} for p1 in scanners[0]}
        result = scanit(scan, rebased0)
        if result is None:
            task_list.append((i, scanners[i]))
            continue
        p1, p2, rot = result
        scanner_locs.add(padd((0, 0, 0), psub(p1, p2)))
        for s in scan:
            x = rotate(s, *rot)
            x = padd(x, psub(p1, p2))
            if x not in rebased0[p1]:
                scanners[0].add(x)
    return len(scanners[0]), scanner_locs


def psub(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]


def padd(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]


def rotate(s, a, b, c, i, j, k):
    return (a * s[i], b * s[j], c * s[k])


def rotations(scan):
    return {r: {rotate(s, *r) for s in scan} for r in ORIENTATIONS}


def mhd(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])


# ======= Part I ========


def part1(data):
    return make_absolute(data)[0]


# ======= Part II ========


def part2(data):
    scanners = make_absolute(data)[1]
    return max(mhd(a, b) for a, b in combinations(scanners, 2))


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    data = parse_data(open(p).read())
    print(part1(data))
    print(part2(data))
