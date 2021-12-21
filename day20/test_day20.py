import solution
from pathlib import Path

RAW_DATA = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


class TestDay:

    data, rules = solution.parse_data(RAW_DATA)

    def test_part_1(self):
        assert solution.part1(self.data, self.rules) == 27

    def test_part_2(self):
        assert solution.part2(self.data, self.rules) == 3080

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data, rules = solution.parse_data(open(p).read())
        assert solution.part1(data, rules) == 5503
        assert solution.part2(data, rules) == 19156
