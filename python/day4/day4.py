from collections import defaultdict, Counter
import datetime
from typing import List
import re


SPLIT_LINE_REGEX = re.compile(r'\[(?P<date>[0-9\- :]+)\] (?P<event>[0-9a-zA-Z #]+)')
GUARD_STARTS = re.compile(r'Guard #(?P<id>[0-9]+)')


def read_lines(location: str) -> List[str]:
    with open(location, 'r') as inp_file:
        return [i.strip() for i in inp_file]


def calculate_sleeping_minutes(start, end):
    number_mins_slept = int((datetime.datetime.strptime(end, '%Y-%m-%d %H:%M') - start).total_seconds() / 60)
    results = []
    for i in range(number_mins_slept):
        results.append((start + datetime.timedelta(minutes=i)).minute)
    return results


def parse_lines(lines: List[str]):
    guard_info = defaultdict(list)
    current_guard, start = 0, 0
    sorted_lines = sorted([SPLIT_LINE_REGEX.search(li).groups() for li in lines], key= lambda group: group[0])
    for l in sorted_lines:
        t, event = l
        if 'falls' in event:
            start = datetime.datetime.strptime(t, '%Y-%m-%d %H:%M')
        elif 'wakes' in event:
            guard_info[current_guard].extend(calculate_sleeping_minutes(start, t))
        else:
            current_guard = int(GUARD_STARTS.search(event).group('id'))
    return guard_info


def part1(data):
    laziest = (0, 0)
    print(len(data))
    for k, v in data.items():
        slept = len(v)
        if slept > laziest[1]:
            laziest = (k, slept)
    count = Counter(data[laziest[0]])
    minute = count.most_common(1)
    minute, _ = minute[0]
    print('Laziest guard: {}, laziest minute: {}'.format(laziest[0], minute))
    print('Result: {}'.format(laziest[0] * minute))

def part2(lines):
    res = parse_lines(lines)
    top_dog = (0, 0)
    for k, v in res.items():
        common = {}
        for i in v:
            if i in common:
                common[i] += 1
            else:
                common[i] = 1
        val = max(common.values())
        if val > top_dog[1]:
            top_dog = (k, val)
    best_min = res[top_dog]
    return top_dog[0] * top_dog[1]


if __name__ == '__main__':
    lines = read_lines('input.txt')
    res = parse_lines(lines)
    part1(res)
    res = part2(lines)
    print(res)