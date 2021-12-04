from pathlib import Path

import solution

RAW_DATA = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class TestDay:

    data = list(map(str, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 198

    def test_part_2(self):
        assert solution.part2(self.data) == 230

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(str, open(p).read().splitlines()))
        assert solution.part1(data) == 4191876
        assert solution.part2(data) == 3414905
