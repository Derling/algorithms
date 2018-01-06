## find missing ranges between low and high in the given array.
# ex) [3, 5] lo=1 hi=10 => answer: [1->2, 4, 6->10]

def missing_ranges(array, low, high):
    missing = []
    start = low
    for i in array:
        if i < start:
            continue
        if i == start:
            start = start + 1
            continue
        missing.append(format_range(start, i - 1))
        start = i + 1
    if start <= high:
        missing.append(format_range(start, high))
    return missing

def format_range(n1, n2):
    if n1 == n2:
        return '{}'.format(n1)
    else:
        return '{0}->{1}'.format(n1, n2)


if __name__ == '__main__':
    r = [3, 5]
    print(missing_ranges(r, 1, 10))
    
'''
go through each number until we find a number that is not one more than the 
previous once we find one that is more than one than the current number
formnat the missing range
'''