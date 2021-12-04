from pathlib import Path

import solution

RAW_DATA = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


class TestDay:

    numbers, boards = solution.load_data(RAW_DATA)

    def test_part_1(self):
        assert solution.part1(self.numbers, self.boards) == 4512

    def test_part_2(self):
        assert solution.part2(self.numbers, self.boards) == 1924

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        numbers, boards = solution.load_data(open(p).read())
        assert solution.part1(numbers, boards) == 69579
        assert solution.part2(numbers, boards) == 14877
