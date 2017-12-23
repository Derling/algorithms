# Sum all the items in a dictionary
# Input {'data1':100,'data2':-54,'data3':247}
# Output 293

def sum_of_values(dic):
    return sum([i for i in dic.values()])


if __name__ == '__main__':
    d = {'data1':100,'data2':-54,'data3':247}
    print(sum_of_values(d))