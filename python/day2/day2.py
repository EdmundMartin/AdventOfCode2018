from typing import List
from collections import defaultdict


def read_file(location: str) -> List[str]:
    with open(location, 'r') as inp_file:
        return [i.strip() for i in inp_file]


def count_tokens(code: str) -> (int, int):
    token_count = defaultdict(lambda: 0)
    for i in code:
        token_count[i] += 1
    values = token_count.values()
    twice_repeat = 1 if 2 in values else 0
    thrice_repeat = 1 if 3 in values else 0
    return twice_repeat, thrice_repeat


def solve_part_one(lines: List[str]):
    two, three = 0, 0
    for l in lines:
        twice, thrice = count_tokens(l)
        two += twice
        three += thrice
    return two * three


def difference(code: str, other: str) -> int:
    if len(code) != len(other):
        return 0
    diff = 0
    for i, _ in enumerate(code):
        if code[i] != other[i]:
            diff += 1
        if diff > 1:
            return diff
    return diff


def common_chars(code: str, other: str) -> str:
    result = ""
    for i, val in enumerate(code):
        if code[i] == other[i]:
            result += val
    return result 


def solve_part_two(lines: List[str]) -> int:
    for first in lines:
        for second in lines[1:]:
            diff = difference(first, second)
            if diff == 1:
                return common_chars(first, second)


if __name__ == '__main__':
    lines = read_file('input.txt')
    print("Part 1 Check code is {}".format(solve_part_one(lines)))
    print("Part 2 Shared Chars is {}".format(solve_part_two(lines)))