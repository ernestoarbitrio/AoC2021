import solution

RAW_DATA = """target area: x=20..30, y=-10..-5"""


class TestDay:
    def test_part1(self):
        _, _, ymin, _ = solution.parse_data(RAW_DATA)
        assert solution.part1(ymin) == 45

    def test_part2(self):
        xmin, xmax, ymin, ymax = solution.parse_data(RAW_DATA)
        assert solution.part2(xmin, xmax, ymin, ymax) == 112

    def test_solution(self):
        input_data = """target area: x=135..155, y=-102..-78"""
        xmin, xmax, ymin, ymax = solution.parse_data(input_data)
        assert solution.part1(ymin) == 5151
        assert solution.part2(xmin, xmax, ymin, ymax) == 968
