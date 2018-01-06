"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
give a single resultant array.
function flatten(input){
}
Example:
Input: var input = [2, 1, [3, [4, 5], 6], 7, [8]];
flatten(input);
Output: [2, 1, 3, 4, 5, 6, 7, 8]
"""

def flatten(array):
    # recursive solution where if an element is a list call the function on it
    # and add the returned array to the base array
    flat_array = []
    for i in array:
        if type(i) == list: # need to unpack elements in list
            flat_array.extend(flatten(i))
        else:
            flat_array.append(i)
    return flat_array


if __name__ == '__main__':
    a = [2, 1, [3, [4, 5], 6], 7, [8]]
    print(flatten(a))