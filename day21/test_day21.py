import solution

RAW_DATA = """Player 1 starting position: 4
              Player 2 starting position: 8"""


class TestDay:

    data = solution.parse_data(RAW_DATA)

    def test_part_1(self):
        assert solution.part1(self.data) == 739785

    def test_part_2(self):
        assert solution.part2(self.data) == 444356092776315

    def test_solution(self):
        input = """Player 1 starting position: 6
                   Player 2 starting position: 10"""
        data = solution.parse_data(input)
        assert solution.part1(data) == 853776
        assert solution.part2(data) == 301304993766094
