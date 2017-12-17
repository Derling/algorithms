# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to construct the following pattern, using a nested loop number.
# 1                                                                                                             
# 22                                                                                                            
# 333                                                                                                           
# 4444                                                                                                          
# 55555                                                                                                         
# 666666                                                                                                        
# 7777777                                                                                                       
# 88888888                                                                                                      
# 999999999

def construct_number_pattern(n):
    # generator, much more elegant and pythonic :) 
    for i in range(1, n + 1):
        yield str(i) * i

def solution():
    # course solution
    for i in range(10):
        print(str(i) * i)

if __name__ == '__main__':
    # grabs valus generated value created by method and prints them
    for pattern in construct_number_pattern(9):
        print(pattern) 