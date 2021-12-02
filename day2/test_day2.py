from pathlib import Path

import solution

RAW_DATA = """forward 5
              down 5
              forward 8
              up 3
              down 8
              forward 2"""


class TestDay:

    data = list(map(solution.parse_entry, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 150

    def test_part_2(self):
        assert solution.part2(self.data) == 900

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(solution.parse_entry, open(p).read().splitlines()))
        assert solution.part1(data) == 1947824
        assert solution.part2(data) == 1813062561
