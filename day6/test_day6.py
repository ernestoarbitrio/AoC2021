from pathlib import Path

import solution

RAW_DATA = """3,4,3,1,2"""


class TestDay:

    data = list(map(solution.parse_data, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 5934

    def test_part_2(self):
        assert solution.part2(self.data, 256) == 26984457539

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(solution.parse_data, open(p).read().splitlines()))
        assert solution.part1(data) == 383160
        assert solution.part2(data, 256) == 1721148811504
