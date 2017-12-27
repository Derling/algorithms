# Write a Python program to remove duplicates from a list.
# Input a = [10,20,30,20,10,50,60,40,80,50,40]
# Output [10, 20, 30, 50, 60, 40, 80]

def remove_duplicates(iterable):
    unique_values = []
    for i in iterable:
        if i not in unique_values:
            unique_values.append(i)
    return unique_values

def solution():
    # course solution
    a = [10,20,30,20,10,50,60,40,80,50,40]
    dup_items = set()
    uniq_items = []
    for x in a:
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

if __name__ == '__main__':
    array = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    print(remove_duplicates(array))
