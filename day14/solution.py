# ---Extended Polymerization---
# https://adventofcode.com/2021/day/14

from pathlib import Path
from collections import Counter


def parse_data(data):
    template = data[0].strip()
    rules = dict(map(lambda x: x.split(" -> "), data[2:]))
    return template, rules


def polymerize(template, rules, iterations=10):
    template_pairs = Counter()
    elements = Counter(template)

    for previous, next in zip(template, template[1:]):
        template_pairs[f"{previous}{next}"] = 1

    for _ in range(iterations):
        new_pairs = Counter()
        for pair, count in template_pairs.items():
            if pair in rules:
                char = rules[pair]
                new_pairs[pair[0] + char] += count
                new_pairs[char + pair[1]] += count
                elements[char] += count

        template_pairs = new_pairs

    return elements.most_common()[0][1] - elements.most_common()[-1][1]


# ========= Part I =========


def part1(polymer, insertions):
    return polymerize(polymer, insertions)


# ========= Part II =========


def part2(polymer, insertions):
    return polymerize(polymer, insertions, 40)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    polymer, insertions = parse_data(open(p).read().splitlines())
    print(part1(polymer, insertions))
    print(part2(polymer, insertions))
