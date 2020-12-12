from typing import List


def count_group_answers(group: str) -> int:
    return len(set([c for c in group]))


def solution(group_answers: List[str]) -> int:
    return sum([count_group_answers(''.join(group.split())) for group in group_answers])


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = f.read().split('\n\n')
        result = solution(input_list)
        print(f'answer for part 1 is {result}')