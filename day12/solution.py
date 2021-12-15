# ---Passage Pathing---
# https://adventofcode.com/2021/day/12

from pathlib import Path
from collections import defaultdict

RAW_DATA = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
"""


def parse_data(data):
    graph = defaultdict(list)
    for line in data:
        start, end = line.split("-")
        graph[start].append(end)
        graph[end].append(start)
    return graph


# ========= Part I =========


def part1(paths):
    num_paths = 0
    stack = [("start", set(["start"]))]

    while stack:
        node, seen = stack.pop()
        for end in paths[node]:
            if end == "end":
                num_paths += 1
                continue
            if end not in seen:
                new_set = seen.copy()
                if end.lower() == end:
                    new_set.add(end)
                stack.append((end, new_set))
    return num_paths


# ========= Part II =========


def part2(paths):
    num_paths = 0
    stack = [("start", set(["start"]), False)]

    while stack:
        node, seen, used = stack.pop()
        for end in paths[node]:
            if end == "end":
                num_paths += 1
                continue
            if end not in seen:
                new_set = seen.copy()
                if end.lower() == end:
                    new_set.add(end)
                stack.append((end, new_set, used))
            elif not used and end != "start" and end != "end":
                new_set = seen.copy()
                if end.lower() == end:
                    new_set.add(end)
                stack.append((end, new_set, True))
    return num_paths


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input = parse_data(open(p).read().splitlines())
    print(part1(input))
    print(part2(input))
