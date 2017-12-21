# Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1 
# j = 0,1, n-1.

# Input
# Input number of rows: 3                                                                                       
# Input number of columns: 4  

# Output
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

def generate_2d_array(rows, columns):
    # list comprehension that generates a 2d array where each element in a 
    # given array is i * j 
    return [[i * j for j in range(columns)] for i in range(rows)]

def solution():
    # course solution
    row_num = int(input("Input number of rows: "))
    col_num = int(input("Input number of columns: "))
    multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

    for row in range(row_num):
        for col in range(col_num):
            multi_list[row][col]= row*col

    print(multi_list)

if __name__ == '__main__':
    i = int(input('Enter the number of rows: '))
    j = int(input('Enter the number of Columns: '))
    print(generate_2d_array(i, j))