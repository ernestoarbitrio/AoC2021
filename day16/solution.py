# ---Packet Decoder---
# https://adventofcode.com/2021/day/16

import math
from pathlib import Path

OPERATIONS_MAP = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: x[0] > x[1],
    6: lambda x: x[0] < x[1],
    7: lambda x: x[0] == x[1],
}


def parse_data(data):
    return "".join((bin(int(data, 16))[2:]))


class BITSTransmission:
    def __init__(self, bits):
        self.bits = bits
        self.pos = 0
        self.version_numbers = 0

    def encode(self, n):
        encode = int(self.bits[self.pos : self.pos + n], 2)
        self.pos += n
        return encode


def decode(bits):
    bits.version_numbers += bits.encode(3)
    type_id = bits.encode(3)
    results = []
    if type_id == 4:
        result = 0
        while True:
            control = bits.encode(1)
            result = result * 16 + bits.encode(4)
            if not control:
                return result

    if bits.encode(1):
        for _ in range(bits.encode(11)):
            results.append(decode(bits))
    else:
        lenght = bits.encode(15)
        end = bits.pos + lenght
        while bits.pos < end:
            results.append(decode(bits))

    return OPERATIONS_MAP.get(type_id)(results)


# ======== Part 1 & 2 ===========


def evaluate(data):
    transmission = BITSTransmission(data)
    evaluated_expression = decode(transmission)
    return transmission.version_numbers, evaluated_expression


if __name__ == "__main__":
    p = Path(__file__).with_name("input.txt")
    input_data = parse_data(open(p).read().strip())
    print(evaluate(input_data))
