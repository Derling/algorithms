VALID_HAIR_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def birth_year_validator(byr: str) -> bool:
    return '2002' >= byr >= '1920'


def issue_year_validator(iyr: str) -> bool:
    return '2020' >= iyr >= '2010'


def expiration_year_validator(eyr: str) -> bool:
    return '2030' >= eyr >= '2020'

def height_validator(hgt: str) -> bool:
    if hgt.endswith('cm'):
        return '193' >= hgt.rstrip('cm') >= '150'

    if hgt.endswith('in'):
        return '76' >= hgt.rstrip('in') >= '59'

    return False


def hair_color_validator(hcl: str) -> bool:
    return hcl.startswith('#') and len(hcl[1:]) == 6 and all([
        '9' >= char >= '0' or 'f' >= char >= 'a'
        for char in hcl[1:]
    ])


def eye_color_validator(ecl: str) -> bool:
    return ecl in VALID_HAIR_COLORS


def passport_id_validator(pid: str) -> bool:
    return all([char.isnumeric() for char in pid]) and len(pid) == 9


PASSPORT_FIELDS_VALIDATORS = {
    'byr': birth_year_validator,
    'iyr': issue_year_validator,
    'eyr': expiration_year_validator,
    'hgt': height_validator,
    'hcl': hair_color_validator,
    'ecl': eye_color_validator,
    'pid': passport_id_validator,
    'cid': lambda i: True
}