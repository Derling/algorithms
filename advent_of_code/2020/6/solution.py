from collections import Counter
from typing import List


def count_similar_answers(group: str) -> int:
    people = len(group.splitlines())
    answer_counts = Counter(''.join(group.split()))
    return sum([1 if answer_count == people else 0 for answer_count in answer_counts.values()])


def count_group_answers(group: str) -> int:
    return len(set([c for c in ''.join(group.split())]))


def solution(group_answers: List[str], answers_vlidator: callable) -> int:
    return sum([answers_vlidator(group) for group in group_answers])


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_list = f.read().split('\n\n')
        result = solution(input_list, count_group_answers)
        print(f'answer for part 1 is {result}')

        result = solution(input_list, count_similar_answers)
        print(f'answer for part 2 is {result}')
