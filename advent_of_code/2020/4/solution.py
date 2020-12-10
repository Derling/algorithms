from typing import List, Mapping

PASSPORT_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # 'cid' is optional so just exclude it from the set

def is_valid_passport(passport_creds: Mapping[str, str]) -> bool:
    print(set(passport_creds.keys()))
    print(not PASSPORT_KEYS - set(passport_creds.keys()))
    return not PASSPORT_KEYS - set(passport_creds.keys())


def solution(batches: List[str]):
    valid_passports = 0
    for batch in batches:
        batch_map = dict([pair.split(':') for pair in batch.split()])
        if is_valid_passport(batch_map):
            valid_passports += 1
    return valid_passports


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_str = f.read()
        batches = input_str.split('\n\n')

        result = solution(batches)
        print(f'part 1 answer is {result}')