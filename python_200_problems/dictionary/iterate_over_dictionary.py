# Write a Python program to iterate over dictionaries using for loops.

def iterate(dic):
    for key, value in dic.items():
        yield '{key} : {value}'.format(key=key, value=value)

def solution():
    # course solution
     d = {'x': 10, 'y': 20, 'z': 30}
     for dict_key, dict_value in d.items():
         print(dict_key,'->',dict_value)

if __name__ == '__main__':
    d = {'x': 10, 'y': 20, 'z': 30}
    for string in iterate(d):
        print(string)