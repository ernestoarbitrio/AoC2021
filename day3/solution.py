# ---Binary Diagnostic---
# https://adventofcode.com/2021/day/3

from pathlib import Path


def _most_common_bits(diag_report):
    data_T = [[int(s) for s in t] for t in zip(*diag_report)]
    return [int(len([i for i in line if i]) >= len(line) / 2) for line in data_T]


def _least_common_bits(diag_report):
    return [int(not b) for b in _most_common_bits(diag_report)]


# ========= Part I =========


def part1(diag_report):
    most_common_bits = "".join(list(map(str, _most_common_bits(diag_report))))
    least_common_bits = "".join(list(map(str, _least_common_bits(diag_report))))

    gamma_rate = int(most_common_bits, 2)
    epsilon_rate = int(least_common_bits, 2)

    return gamma_rate * epsilon_rate


# ========= Part II =========


def part2(diag_report):
    def rating(diag_report, bit_criteria):
        no_of_bits = len(diag_report[0])
        for i in range(no_of_bits):
            bit_results = bit_criteria(diag_report)
            diag_report = [el for el in diag_report if int(el[i]) == bit_results[i]]
            if len(diag_report) == 1:
                return int(diag_report[0], 2)

    return rating(diag_report, _most_common_bits) * rating(
        diag_report, _least_common_bits
    )


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = list(map(str, open(p).read().splitlines()))
    print(part1(input_data))
    print(part2(input_data))
