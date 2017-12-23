# Write a Python script to concatenate following dictionaries to create a new one
# Input
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Output
# {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def concatenate(*args):
    d = {}
    for dic in args:
        d.update(dic)
    return d

def solution():
    # course solution
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4 = {}
    for d in (dic1, dic2, dic3): 
        dic4.update(d)
    print(dic4)

if __name__ == '__main__':
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    print(concatenate(dic1,dic2,dic3))