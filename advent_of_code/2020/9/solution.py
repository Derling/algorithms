from typing import List


def solution2(data: List[int]) -> int:
    invalid_num = solution(data)
    for start in range(len(data)):
        for end in range(start + 1, len(data)):
            current_range = data[start: end]
            range_sum = sum(current_range)

            if sum(current_range) == invalid_num:
                return min(current_range) + max(current_range)
            
            if range_sum > invalid_num:
                break


def is_valid_number(preamble: List[int], number: int) -> bool:
    nums = set(preamble)
    for num in nums:
        if number - num in nums:
            return True
    return False


def solution(data: List[int], preamble: int = 25) -> int:
    for i in range(preamble, len(data)):
        num = data[i]
        if not is_valid_number(data[i - preamble: i], num):
            return num


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = list(map(int, f.readlines()))
        result = solution(input_list)
        print(f'part 1 answer is {result}')

        result = solution2(input_list)
        print(f'part 2 answer is {result}')