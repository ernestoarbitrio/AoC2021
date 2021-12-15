from pathlib import Path

import solution

RAW_DATA = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


class TestDay:

    data = list(map(solution.parse_data, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 15

    def test_part_2(self):
        assert solution.part2(self.data) == 1134

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(solution.parse_data, open(p).read().splitlines()))
        assert solution.part1(data) == 633
        assert solution.part2(data) == 1050192
