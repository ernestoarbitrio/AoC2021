from pathlib import Path
import solution

RAW_DATA = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


class TestDay:

    data = list(map(solution.parse_data, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 40

    def test_part_2(self):
        assert solution.part2(self.data) == 315

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = list(map(solution.parse_data, open(p).read().splitlines()))
        assert solution.part1(data) == 583
        assert solution.part2(data) == 2927
