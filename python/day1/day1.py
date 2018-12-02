from typing import List


def read_file(location: str) -> List[int]:
    results = []
    with open(location) as inpfile:
        for line in inpfile:
            res = int(line.strip())
            results.append(res)
    return results

def repeating_freq(results: List[int]) -> int:
    freq = 0
    seen = set()
    while True:
        for i in results:
            if freq in seen:
                return freq
            seen.add(freq)
            freq += i
        

if __name__ == '__main__':
    results = read_file("input.txt")
    frequency = sum(results)
    print("Correct frequency is {}".format(frequency))
    print("First repreating frequency is {}".format(repeating_freq(results)))