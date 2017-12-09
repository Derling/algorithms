# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]


def merge_intervals(intervals):
    ''' intervals are sorted '''
    merge = [intervals[0]] # add first interval to merged array
    for i in intervals:
        # check if starting number in current range is in the current range
        if i[0] < merge[-1][1]:
            # increase the range of the last range
            merge[-1][1] = i[-1]
        else:
            merge.append(i)
    return merge

def merge(collection):
    # course solution
    i = 0
    while i < len(collection)-1:
        #  print(org_intervals[i])
        if collection[i+1][0] < collection[i][1]:
            collection[i][1] = collection[i+1][1]
            del collection[i+1]
            i = i - 1
        i = i + 1
    return collection
    

if __name__ == '__main__':
    print(merge_intervals(
            [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]
            )
        )
    print(merge([[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]))