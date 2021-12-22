# ---Reactor Reboot---
# https://adventofcode.com/2021/day/22

from pathlib import Path
import re


def parse_data(line):
    on_off, coords = line.split()
    coords_groups = re.match(
        r"x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", coords
    )
    return (on_off == "on", tuple(int(x) for x in coords_groups.groups()))


class Cuboid:
    def __init__(self, bounds):
        self.bounds = bounds
        self.vacuums = []

    def remove(self, bounds):
        int_bounds = self._intersect_bounds(self.bounds, bounds)
        if not int_bounds:
            return
        for vacuum in self.vacuums:
            vacuum.remove(int_bounds)
        self.vacuums.append(Cuboid(int_bounds))

    @property
    def volume(self):
        x1, x2, y1, y2, z1, z2 = self.bounds
        return (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) - sum(
            vacuum.volume for vacuum in self.vacuums
        )

    def _intersect_ranges(self, r11, r12, r21, r22):
        if r21 > r12 or r11 > r22:
            return None
        nums = sorted([r11, r12, r21, r22])
        return [nums[1], nums[2]]

    def _intersect_bounds(self, bounds1, bounds2):
        x11, x12, y11, y12, z11, z12 = bounds1
        x21, x22, y21, y22, z21, z22 = bounds2
        x = self._intersect_ranges(x11, x12, x21, x22)
        y = self._intersect_ranges(y11, y12, y21, y22)
        z = self._intersect_ranges(z11, z12, z21, z22)
        return None if not all((x, y, z)) else x + y + z


# ========= Part I =========


def part1(data):
    cube_on = set()
    for is_on, bounds in data:
        x1, x2, y1, y2, z1, z2 = bounds
        for x in range(max(-50, x1), min(51, x2 + 1)):
            for y in range(max(-50, y1), min(51, y2 + 1)):
                for z in range(max(-50, z1), min(51, z2 + 1)):
                    cube_on.add((x, y, z)) if is_on else cube_on.discard((x, y, z))
    return len(cube_on)


# ========= Part II =========


def part2(data):

    cuboids = []
    for is_on, bounds in data:
        for cuboid in cuboids:
            cuboid.remove(bounds)
        if is_on:
            cuboids.append(Cuboid(bounds))

    return sum(cuboid.volume for cuboid in cuboids)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    data = open(p).read().splitlines()
    input_data = list(map(parse_data, data))
    print(part1(input_data))
    print(part2(input_data))
