# ---Sonar Sweep---
# https://adventofcode.com/2021/day/1

from itertools import starmap
from operator import lt

# ========= Data =========
input_data = list(map(int, open("input.txt").read().splitlines()))

# ========= Part I =========
couples = zip(input_data, input_data[1:])

print(sum(list(starmap(lt, couples))))


# ========= Part II =========
windows = zip(input_data, input_data[1:], input_data[2:])
ws = list(map(sum, windows))

print(sum(list(starmap(lt, zip(ws, ws[1:])))))
