from pathlib import Path

import solution

RAW_DATA = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class TestDay:

    data = list(map(solution.parse_data, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 5

    def test_part_2(self):
        assert solution.part2(self.data) == 12

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(solution.parse_data, open(p).read().splitlines()))
        assert solution.part1(data) == 7674
        assert solution.part2(data) == 20898
