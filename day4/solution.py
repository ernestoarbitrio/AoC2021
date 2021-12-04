# ---Big Squid---
# https://adventofcode.com/2021/day/4

from pathlib import Path


def load_data(data):
    def parse_board(board):
        return [[[int(num), 0] for num in el.strip().split(" ") if num] for el in board]

    input_data = [el for el in list(map(str, data.splitlines())) if el]
    random_numbers = list(map(int, input_data[0].split(",")))
    boards = list(map(parse_board, list(zip(*[iter(input_data[1:])] * 5))))
    return random_numbers, boards


def mark_on_boards(number, boards):
    for board in boards:
        for row in board:
            for n in row:
                if n[0] == number:
                    n[1] = 1


def check_winner(board):
    drawn_board = [[el[1] for el in line] for line in board]
    for i, line in enumerate(drawn_board):
        if sum(line) == 5 or sum([line[i] for line in drawn_board]) == 5:
            return True
    return False


def bingo(numbers, boards, let_squid_win=False):
    for number in numbers:
        mark_on_boards(number, boards)
        for board in boards:
            if check_winner(board):
                if not let_squid_win:
                    return number, board
                boards.remove(board)
        if let_squid_win:
            if len(boards) == 0:
                return number, board


def unmarked_numbers(board):
    return list(map(sum, [[n[0] for n in line if not n[1]] for line in board]))


# ========= Part I =========


def part1(random_numbers, boards):
    num, winner = bingo(random_numbers, boards)
    return sum(unmarked_numbers(winner)) * num


# ========= Part II =========


def part2(random_numbers, boards):
    num, winner = bingo(random_numbers, boards, True)
    return sum(unmarked_numbers(winner)) * num


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    random_numbers, boards = load_data(open(p).read())
    print(part1(random_numbers, boards))
    print(part2(random_numbers, boards))
