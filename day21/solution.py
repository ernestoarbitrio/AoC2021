# ---Dirac Dice---
# https://adventofcode.com/2021/day/21

import itertools
from functools import lru_cache

THROWS = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]


def parse_data(data):
    return [int(line.strip().split()[-1]) for line in data.splitlines()]


@lru_cache(maxsize=None)
def calc_quantum(a_pos, a_score, b_pos, b_score, a_turn):
    if a_score >= 21:
        return 1, 0
    if b_score >= 21:
        return 0, 1
    pos = a_pos if a_turn else b_pos
    new_positions = [(pos + throw - 1) % 10 + 1 for throw in THROWS]
    if a_turn:
        subgames = (
            calc_quantum(new_p, a_score + new_p, b_pos, b_score, False)
            for new_p in new_positions
        )
    else:
        subgames = (
            calc_quantum(a_pos, a_score, new_p, b_score + new_p, True)
            for new_p in new_positions
        )
    return sum(a for a, _ in subgames), sum(b for _, b in subgames)


# ========= Part I =========


def part1(data):
    a_pos, b_pos = data[0], data[1]
    a_score = 0
    b_score = 0
    die = 0
    a_turn = True
    while a_score < 1000 and b_score < 1000:
        die += 3
        mov_pos = 3 * die - 3
        if a_turn:
            a_pos = (a_pos + mov_pos - 1) % 10 + 1
            a_score += a_pos
        else:
            b_pos = (b_pos + mov_pos - 1) % 10 + 1
            b_score += b_pos
        a_turn = not a_turn
    return (a_score if a_score < b_score else b_score) * die


# ========= Part II =========


def part2(data):
    a_pos, b_pos = data[0], data[1]
    return max(calc_quantum(a_pos, 0, b_pos, 0, True))


if __name__ == "__main__":
    input = """Player 1 starting position: 6
               Player 2 starting position: 10"""
    data = parse_data(input)
    print(part1(data))
    print(part2(data))
