"""
Given a collection of intervals, merge all overlapping intervals.
For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

def merge_intervals(intervals):
    merge = [intervals[0]]
    for i in intervals:
        if i[0] < merge[-1][1]:
            merge[-1][1] = i[1]
        else:
            merge.append(i)
    return merge

if __name__ == '__main__':
    a = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(a))

'''
assuming the intervals are sorted
add the first interval to the merged array
iterate throught the intervals array and check if the
lower bounds of the ith interval is less than the upper bound of the last 
interval in our merged array 
if so that interval lies between the last 
interval in the merged array
else append that interval to the merged array because it does not lie within
any other intervals
'''