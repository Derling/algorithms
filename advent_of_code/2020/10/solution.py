from collections import defaultdict
from typing import List

def solution(jolts: List[int]) -> int:
    jolt_diffs = defaultdict(int)
    current_jolt = 0
    for jolt in sorted(jolts):
        diff = jolt - current_jolt
        if diff == 1 or diff == 3:
            jolt_diffs[diff] += 1
        current_jolt = jolt
    jolt_diffs[3] += 1
    return jolt_diffs[3] * jolt_diffs[1]

if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = list(map(int, f.readlines()))
        result = solution(input_list)

        print(f'part 1 answer is {result}')
