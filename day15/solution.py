# ---Chiton---
# https://adventofcode.com/2021/day/15

from pathlib import Path
from heapq import heappop, heappush


def parse_data(line):
    return [int(x) for x in line.strip()]


def expanded_matrix(data):
    heap = [(0, 0, 0)]
    seen = {(0, 0)}
    while heap:
        distance, x, y = heappop(heap)
        if x == 5 * len(data) - 1 and y == 5 * len(data[0]) - 1:
            return distance

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x_, y_ = x + dx, y + dy
            if x_ < 0 or y_ < 0 or x_ >= 5 * len(data) or y_ >= 5 * len(data):
                continue

            a, am = divmod(x_, len(data))
            b, bm = divmod(y_, len(data[0]))
            n = ((data[am][bm] + a + b) - 1) % 9 + 1

            if (x_, y_) not in seen:
                seen.add((x_, y_))
                heappush(heap, (distance + n, x_, y_))


# ========= Part I =========


def part1(input_data):
    path = {}

    def find_path(x, y):
        if (x, y) in path:
            return path[(x, y)]
        if x < 0 or x >= len(input_data) or y < 0 or y >= len(input_data[x]):
            return 1e9
        if x == len(input_data) - 1 and y == len(input_data[x]) - 1:
            return input_data[x][y]
        ans = input_data[x][y] + min(find_path(x + 1, y), find_path(x, y + 1))
        path[(x, y)] = ans
        return ans

    return find_path(0, 0) - input_data[0][0]


# ========= Part II =========


def part2(input_data):
    return expanded_matrix(input_data)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    data = list(map(parse_data, p.read_text().splitlines()))
    print(part1(data))
    print(part2(data))
