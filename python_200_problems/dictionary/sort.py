# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary :  {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}                                                         
# Dictionary in ascending order by value :  [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)]                            
# Dictionary in descending order by value :  [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]

def sort(dic, descending=False):
    sorted_dict = sorted(dic.items(), key=lambda i:i[0], reverse=descending)
    return sorted_dict 

def solution():
    # course solution
    import operator
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    print('Original dictionary : ',d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0))
    print('Dictionary in ascending order by value : ',sorted_d)
    sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
    print('Dictionary in descending order by value : ',sorted_d)


if __name__ == '__main__':
    d = {0: 0, 1: 2, 2: 1, 3: 4, 4: 3}
    print(sort(d)) # print in ascending order
    print(sort(d, True)) # print in descending order