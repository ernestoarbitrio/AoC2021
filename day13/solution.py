# ---Transparent Origami---
# https://adventofcode.com/2021/day/13

from pathlib import Path


def parse_data(data):
    dots, folds = [p.strip().split("\n") for p in data.strip().split("\n\n")]
    dots = list(map(lambda x: tuple(map(int, x.split(","))), dots))
    folds = list(
        map(
            lambda x: tuple(map(str, x.strip().replace("fold along ", "").split("="))),
            folds,
        )
    )
    return set(dots), folds


def fold(dots, folds, show_code=False):
    for axis, fold_point in folds:
        new_coords = []

        max_x = max(dots, key=lambda x: x[0])[0]
        max_y = max(dots, key=lambda x: x[1])[1]

        for x, y in dots:
            if axis == "x" and x > int(fold_point):
                new_coords.append((max_x - x, y))
            elif axis == "y" and y > int(fold_point):
                new_coords.append((x, max_y - y))
            else:
                new_coords.append((x, y))

        dots = set(new_coords)

    if show_code:
        code = ""
        range_x = max(dots, key=lambda x: x[0])[0] + 1
        range_y = max(dots, key=lambda x: x[1])[1] + 1
        for y in range(range_y):
            code += (
                "".join(["#" if (x, y) in dots else " " for x in range(range_x)]) + "\n"
            )
        return code

    return len(dots)


# ========= Part I =========


def part1(dots, folds):
    return fold(dots, folds)


# ========= Part II =========


def part2(dots, folds):
    return fold(dots, folds, show_code=True)


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    dots, folds = parse_data(open(p).read())
    print(fold(dots, folds[:1]))
    print(fold(dots, folds, show_code=True))
