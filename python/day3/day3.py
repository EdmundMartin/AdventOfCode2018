from typing import List, Dict, Tuple
from collections import defaultdict


def read_lines(location: str) -> List[str]:
    with open(location, 'r') as inp_file:
        return [i.strip() for i in inp_file]


def parse_lines(lines: List[str]) -> List[Dict]:
    parsed_data = []
    for line in lines:
        res = line.split(' ')
        x, y = res[2].replace(':', '').split(',')
        width, height = res[3].split('x')
        parsed_data.append({
            'claim_id': int(res[0].replace('#', '')),
            'x_value': int(x), 
            'y_value': int(y),
            'width': int(width),
            'height': int(height)
        })
    return parsed_data


def get_x_squares(item: Dict[str, int]) -> List[Tuple[int, int]]:
    result = []
    for x in range(item['width']):
        result.append((x + item['x_value'], item['y_value']))
    return result

def get_y_squares(item: List[Tuple[int, int]], height: int) -> List[Tuple[int, int]]:
    return [(x, y+i) for x, y in item for i in range(height)]
        

def matching_squares(parsed_data: List[Dict[str, int]]) -> int:
    squares = defaultdict(lambda: 0)
    for item in parsed_data:
        x_claim = get_x_squares(item)
        all_squares = get_y_squares(x_claim, item['height'])
        square_ids = ['{}_{}'.format(x, y) for x, y in all_squares]
        for sq in square_ids:
            squares[sq] += 1
    overlaps = [v for v in squares.values() if v > 1]
    return len(overlaps)


def unique_claims(parsed_data: List[Dict[str, int]]):
    squares = defaultdict(list)
    for item in parsed_data:
        claim_id = item['claim_id']
        x_claim = get_x_squares(item)
        all_squares = get_y_squares(x_claim, item['height'])
        for square in all_squares:
            squares[square].append(claim_id)
    
    all_claims = [i['claim_id'] for i in parsed_data]
    overlapping_claims = set()
    for k, v in squares.items():
        if len(v) > 1:
            for i in v:
                overlapping_claims.add(i)
    return set(all_claims) - overlapping_claims


if __name__ == '__main__':
    lines = read_lines('input.txt')
    data = parse_lines(lines)
    part1 = matching_squares(data)
    print('Found {} overlapping squares'.format(part1))
    part2 = unique_claims(data)
    print('Unique claim: {}'.format(part2))
