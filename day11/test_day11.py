from pathlib import Path

import solution

RAW_DATA = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""


class TestDay:

    input_data = RAW_DATA.strip().split("\n")
    board, adjacent = solution.parse_data(input_data)

    def test_part_1(self):
        assert solution.part1(self.board, self.adjacent) == 1656

    def test_part_2(self):
        assert solution.part2(self.board, self.adjacent) == 195

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        input_data = p.open().read().strip().split("\n")
        board, adjacent = solution.parse_data(input_data)
        assert solution.part1(board, adjacent) == 1702
        assert solution.part2(board, adjacent) == 251
