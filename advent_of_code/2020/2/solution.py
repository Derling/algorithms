from typing import List

def is_valid_toboggan_password(password_range: tuple, char: str, password: str) -> bool:
    # logic for part 2
    char_position1 = password[password_range[0] - 1]
    char_position2 = password[password_range[1] - 1]
    return (
        char_position1 == char and char_position2 != char
    ) or (
        char_position1 != char and char_position2 == char
    )


def is_valid_sled_password(password_range: tuple, char: str, password: str) -> bool:
    # logic for part 1
    min_limit, max_limit = password_range
    char_count = password.count(char)
    return max_limit >= char_count >= min_limit


def solution(policies: List[str], password_validator: callable) -> int:
    # solves for part 1 and 2(dependant on the policy function)
    count = 0
    for policy in policies:
        password_range, char, password = policy.split()
        password_range = tuple(map(int, password_range.split('-')))
        char = char[0]  # remove ':' at end of string
        count += 1 if password_validator(password_range, char, password) else 0
    return count


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(fpath) as f:
        input_list = f.readlines()

        valid_passwords = solution(input_list, is_valid_sled_password)
        print(f'part 1 answer is {valid_passwords}')

        valid_passwords = solution(input_list, is_valid_toboggan_password)
        print(f'part 2 answer is {valid_passwords}')
