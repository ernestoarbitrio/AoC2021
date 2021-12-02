from pathlib import Path

import solution

RAW_DATA = """199
              200
              208
              210
              200
              207
              240
              269
              260
              263"""


class TestDay:

    data = list(map(int, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 7

    def test_part_2(self):
        assert solution.part2(self.data) == 5

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(int, open(p).read().splitlines()))
        assert solution.part1(data) == 1466
        assert solution.part2(data) == 1491
