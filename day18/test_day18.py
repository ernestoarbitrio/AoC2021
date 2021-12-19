import solution
from pathlib import Path

RAW_DATA = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


class TestDay:
    data = solution.parse_data(RAW_DATA)

    def test_part1(self):
        assert solution.part1(self.data) == 4140

    def test_part2(self):
        assert solution.part2(self.data) == 3993

    def test_solution(self):
        p = Path(__file__).with_name("input.txt")
        input_data = solution.parse_data(open(p).read())
        assert solution.part1(input_data) == 3756
        assert solution.part2(input_data) == 4585
