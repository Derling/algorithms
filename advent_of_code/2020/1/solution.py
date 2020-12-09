import os
from typing import List


def solution_part1(expense_report: List[int], needed_sum: int = 2020) -> int:
    report_set = set(expense_report)
    for entry in report_set:
        if (other_entry := abs(entry - needed_sum)) in report_set:
            return entry * other_entry
    return None


def solution_part2(expense_report: List[int], needed_sum: int = 2020) -> int:
    report_set = set(expense_report)

    for idx1, entry1 in enumerate(report_set):
        for idx2, entry2 in enumerate(report_set):
            if idx1 == idx2:
                continue
            current_sum = entry1 + entry2
            if((entry3 := needed_sum - current_sum) in report_set):
                return entry1 * entry2 * entry3

    return None


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_path) as f:
        input_list = list(map(int, f.readlines()))

        result = solution_part1(input_list)
        if result:
            print(f'part 1 answer is {result}')

        result = solution_part2(input_list)
        if result:
            print(f'part 2 answer is {result}')
