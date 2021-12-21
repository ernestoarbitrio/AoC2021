import solution
from pathlib import Path


class TestDay:
    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = solution.parse_data(open(p).read())
        assert solution.part1(data) == 332
        assert solution.part2(data) == 8507
