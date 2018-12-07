

def read_file(filename: str) -> str:
    f = open(filename)
    res = f.read()
    f.close()
    return res


def reaction(first: str, second: str) -> bool:
    return first != second and first.lower() == second.lower()


def remove_reactant(polymer: str, to_remove: str) -> str:
    for i in [to_remove.upper(), to_remove.lower()]:
        polymer = polymer.replace(i, '')
    return polymer


def reduce_polymer(poly: str) -> str:
    remaining = []
    for item in poly:
        if remaining and reaction(remaining[-1], item):
            remaining.pop()
        else:
            remaining.append(item)
    return remaining


def shortest_polymer(lines: str):
    unique_chars = ''.join(set(lines.lower()))
    min_len = None
    for c in unique_chars:
        curren_len = reduce_polymer(remove_reactant(lines, c))
        if min_len is None:
            min_len = len(curren_len)
        elif len(curren_len) < min_len:
            min_len = len(curren_len)
    return min_len


if __name__ == '__main__':
    lines = read_file('input.txt')
    remaining_polymers = reduce_polymer(lines)
    print('Length of remaining polymers: {}'.format(len(remaining_polymers)))
    min_len = shortest_polymer(lines)
    print('Minimum length: {}'.format(min_len))