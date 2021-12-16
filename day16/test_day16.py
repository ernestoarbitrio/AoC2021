from pathlib import Path
import solution

RAW_DATA = """EE00D40C82306000102203022"""


class TestDay:
    def test_demo_data(self):
        data = solution.parse_data(RAW_DATA.strip())
        assert solution.evaluate(data) == (14, 3)

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        data = solution.parse_data(open(p).read().strip())
        assert solution.evaluate(data) == (920, 10185143721112)
