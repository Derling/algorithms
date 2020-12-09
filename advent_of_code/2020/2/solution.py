from typing import List


def is_valid_policy(policy: str):
    limit, char, password = policy.split()
    char = char[0]  # remove ':'
    min_limit, max_limit = list(map(int, limit.split('-')))
    char_count = password.count(char)
    return max_limit >= char_count >= min_limit 


def solution_1(policies: List[str]) -> int:
    count = 0
    for policy in policies:
        count += 1 if is_valid_policy(policy) else 0
    return count


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(fpath) as f:
        input_list = f.readlines()
        valid_passwords = solution_1(input_list)
        print(f'part 1 answer is {valid_passwords}')
