# ---Trick Shot---
# https://adventofcode.com/2021/day/17

import re


def parse_data(data):
    return map(int, re.findall(r"-?\d+", data))


def find_distinct_velocity(xmin, xmax, ymin, ymax, v0xmin):
    total = 0

    for v0x in range(v0xmin, xmax + 1):
        for v0y in range(ymin, -ymin):
            x, y = 0, 0
            vx, vy = v0x, v0y

            while x <= xmax and y >= ymin:
                if x >= xmin and y <= ymax:
                    total += 1
                    break

                x, y = (x + vx, y + vy)
                vy -= 1

                if vx > 0:
                    vx -= 1

    return total


# ========= Part I =========


def part1(ymin):
    return ymin * (ymin + 1) // 2


# ========= Part II =========


def part2(xmin, xmax, ymin, ymax):
    v0xmin = int((xmin * 2) ** 0.5)
    return find_distinct_velocity(xmin, xmax, ymin, ymax, v0xmin)


if __name__ == "__main__":
    input_data = """target area: x=135..155, y=-102..-78"""
    xmin, xmax, ymin, ymax = parse_data(input_data)
    print(part1(ymin))
    print(part2(xmin, xmax, ymin, ymax))
