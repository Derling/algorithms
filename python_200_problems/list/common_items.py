# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

def common_items(iter1, iter2):
    # generator funcction
    for item in iter1:
        if item in iter2:
            yield item

def solution():
    # course solution    
    color1 = "Red", "Green", "Orange", "White"
    color2 = "Black", "Green", "White", "Pink"
    print(set(color1) & set(color2))

if __name__ == '__main__':
    color1 = ["Red", "Green", "Orange", "White"]
    color2 = ["Black", "Green", "White", "Pink"]
    for color in common_items(color1, color2):
        print(color, end=' ')