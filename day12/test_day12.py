from pathlib import Path

import solution

RAW_DATA = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""


class TestDay:

    data = solution.parse_data(RAW_DATA.splitlines())

    def test_part_1(self):
        assert solution.part1(self.data) == 19

    def test_part_2(self):
        assert solution.part2(self.data) == 103

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = solution.parse_data(open(p).read().splitlines())
        assert solution.part1(data) == 3761
        assert solution.part2(data) == 99138
