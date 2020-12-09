import os
from typing import List


def solution(expense_report: List[int], needed_sum: int = 2020) -> int:
    report_set = set(expense_report)
    for entry in report_set:
        if (other_entry := abs(entry - needed_sum)) in report_set:
            return entry * other_entry
    return None


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path) as f:
        input_list = list(map(int, f.readlines()))
        result = solution(input_list)
        if result:
            print(f'Answer is {result}')
