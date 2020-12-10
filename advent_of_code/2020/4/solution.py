from utils import PASSPORT_FIELDS_VALIDATORS
from typing import List, Mapping

Passport = Mapping[str, str]
PASSPORT_KEYS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}  # 'cid' is optional so just exclude it from the set

def contains_required_fields(passport_creds: Passport) -> bool:
    return not PASSPORT_KEYS - set(passport_creds.keys())

def check_passport_fields(passport_creds: Passport, validators: Mapping[str, callable] = PASSPORT_FIELDS_VALIDATORS) -> bool:
    return all([validators[field](value) for field, value in passport_creds.items()])


def solution(batches: List[str], validate_fields: bool = False):
    valid_passports = 0
    for batch in batches:
        batch_map = dict([pair.split(':') for pair in batch.split()])

        if contains_required_fields(batch_map):
            if not validate_fields:
                valid_passports += 1
            else:
                valid_passports += 1 if check_passport_fields(batch_map) else 0

    return valid_passports


if __name__ == '__main__':
    import os
    fpath = os.path.join(os.path.dirname(__file__), 'input.txt')

    with open(fpath) as f:
        input_str = f.read()
        batches = input_str.split('\n\n')

        result = solution(batches)
        print(f'part 1 answer is {result}')

        result = solution(batches, validate_fields=True)
        print(f'part 2 answer is {result}')
