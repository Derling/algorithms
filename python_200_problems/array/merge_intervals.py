# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Given a collection of intervals which are already sorted by start number, merge all overlapping intervals.
# For example,
# Given [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]],
# return [[1, 10], [11, 18], [19, 22]]


def merge_intervals(intervals):
    merge = [intervals[0]]
    for i in intervals:
        if i[0] in range(merge[-1][0], merge[-1][1]):
            merge[-1][1] = i[-1]
        else:
            merge.append(i)
    return merge

if __name__ == '__main__':
    print(merge_intervals(
            [[1,3],[2,6],[5,10],[11,16],[15,18],[19,22]]))