from pathlib import Path

import solution

RAW_DATA = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


class TestDay:

    dots, folds = solution.parse_data(RAW_DATA)
    part2_expected = """
#####
#   #
#   #
#   #
#####
"""
    final_expectation = """
#  #  ##   ##    ## ###  #### #  #  ## 
#  # #  # #  #    # #  # #    #  # #  #
#### #    #  #    # ###  ###  #### #   
#  # # ## ####    # #  # #    #  # #   
#  # #  # #  # #  # #  # #    #  # #  #
#  #  ### #  #  ##  ###  #### #  #  ##
"""

    def test_part_1(self):
        assert solution.part1(self.dots, self.folds[1:]) == 17

    def test_part_2(self):
        assert (
            solution.part2(self.dots, self.folds).strip() == self.part2_expected.strip()
        )

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        dots, folds = solution.parse_data(open(p).read())
        assert solution.part1(dots, folds[:1]) == 704
        assert solution.part2(dots, folds).strip() == self.final_expectation.strip()
