from pathlib import Path

import solution

RAW_DATA = """16,1,2,0,4,2,7,1,2,14"""


class TestDay:

    crabs = list(map(solution.parse_data, RAW_DATA.splitlines()))[0]

    def test_part_1(self):
        assert solution.part1(self.crabs) == 37

    def test_part_2(self):
        assert solution.part2(self.crabs) == 168

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(solution.parse_data, open(p).read().splitlines()))[0]
        assert solution.part1(data) == 356992
        assert solution.part2(data) == 101268110
