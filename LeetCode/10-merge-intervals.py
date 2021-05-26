'''
Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

'''
def merge(intervals):
    intervals.sort()
    merged = []
    for i in range(len(intervals)):
        if merged == []:
            merged.append(intervals[i])
        else:
            previous_end = merged[-1][1] # pick up the end of the last merged
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if previous_end >= current_start: # overlap
                # update the end of the last merged
                merged[-1][1] = max(previous_end,current_end)
            else:
                merged.append(intervals[i])
    return merged



merge([[1,3],[2,6],[8,10],[15,18]])