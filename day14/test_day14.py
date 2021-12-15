from pathlib import Path

import solution

RAW_DATA = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


class TestDay:

    polymer, insertions = solution.parse_data(RAW_DATA.splitlines())

    def test_part_1(self):
        assert solution.part1(self.polymer, self.insertions) == 1588

    def test_part_2(self):
        assert solution.part2(self.polymer, self.insertions) == 2188189693529

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        polymer, insertions = solution.parse_data(open(p).read().splitlines())
        assert solution.part1(polymer, insertions) == 3259
        assert solution.part2(polymer, insertions) == 3459174981021
