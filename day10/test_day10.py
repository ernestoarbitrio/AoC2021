from pathlib import Path

import solution

RAW_DATA = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


class TestDay:

    data = list(map(str, RAW_DATA.splitlines()))

    def test_part_1(self):
        assert solution.part1(self.data) == 26397

    def test_part_2(self):
        assert solution.part2(self.data) == 288957

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        input_data = list(map(str, open(p).read().splitlines()))
        assert solution.part1(input_data) == 369105
        assert solution.part2(input_data) == 3999363569
