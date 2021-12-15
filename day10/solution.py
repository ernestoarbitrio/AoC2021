# ---Smoke Basin---
# https://adventofcode.com/2021/day/10

from pathlib import Path
import statistics

MAPPING = {"<": ">", "[": "]", "{": "}", "(": ")"}


# ========= Part I =========


def part1(input_data):
    points = {")": 3, "]": 57, "}": 1197, ">": 25137}
    count = 0
    for line in input_data:
        d = []
        for c in line:
            if c in MAPPING.keys():
                d.append(c)
            else:
                e = d.pop()
                if MAPPING[e] != c:
                    count += points[c]
    return count


# ========= Part II =========


def part2(input_data):
    corrupted = []
    completion = []
    points = {")": 1, "]": 2, "}": 3, ">": 4}

    for line in input_data:
        d = []
        for c in line:
            if c in MAPPING.keys():
                d.append(c)
            else:
                e = d.pop()
                if MAPPING[e] != c:
                    corrupted.append(line)
        if line not in corrupted:
            completion.append(list(reversed([MAPPING[elem] for elem in d])))

    scores = []
    for line in completion:
        total_score = 0
        for char in line:
            total_score *= 5
            total_score = total_score + points[char]
        scores.append(total_score)

    sorted_ = list(sorted(scores))

    return statistics.median(sorted_)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = list(map(str, open(p).read().splitlines()))
    print(part1(input_data))
    print(part2(input_data))
