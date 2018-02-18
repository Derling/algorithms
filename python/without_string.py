'''
Given two strings, base and remove, return a version of the base string where all instances of the remove string have been removed (not case sensitive). You may assume that the remove string is length 1 or more. Remove only non-overlapping instances, so with "xxx" removing "xx" leaves "x".

withoutString("Hello there", "llo") → "He there"
withoutString("Hello there", "e") → "Hllo thr"
withoutString("Hello there", "x") → "Hello there"
'''

def without_string(base, remove):
    # case insensitive comparisons, so i validate in lower case
    new_string = []
    str_index = 0
    first_char = remove[0].lower()
    while str_index < len(base):
        char = base[str_index].lower()
        if char == first_char:
            sub_range = str_index + len(remove)
            sub = base[str_index: sub_range].lower()
            if sub != remove.lower():
                new_string.extend(sub)
            str_index = sub_range
        else:
            new_string.append(char)
            str_index += 1
    return ''.join(new_string)

if __name__ == '__main__':
    print(without_string('hello there', 'llo'))