"""
    给你一个区间数组 intervals ，其中intervals[i] = [starti, endi] ，且每个starti 都 不同 。区间 i 的 右侧区间 可以记作区间 j ，并满
足 startj>= endi ，且 startj 最小化 。返回一个由每个区间 i 的 右侧区间 的最小起始位置组成的数组。如果某个区间 i 不存在对应的 右侧区间 ，则
下标 i 处的值设为 -1 。

示例 1：
    输入：intervals = [[1,2]]
    输出：[-1]
    解释：集合中只有一个区间，所以输出-1。

示例 2：
    输入：intervals = [[3,4],[2,3],[1,2]]
    输出：[-1,0,1]
    解释：对于 [3,4] ，没有满足条件的“右侧”区间。
    对于 [2,3] ，区间[3,4]具有最小的“右”起点;
    对于 [1,2] ，区间[2,3]具有最小的“右”起点。

示例 3：
    输入：intervals = [[1,4],[2,3],[3,4]]
    输出：[-1,2,-1]
    解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
    对于 [2,3] ，区间 [3,4] 有最小的“右”起点。

提示：
    1 <=intervals.length <= 2 * 104
    intervals[i].length == 2
    -106 <= starti <= endi <= 106
    每个间隔的起点都 不相同
"""
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        return self.solve_1(intervals)

    @classmethod
    def solve_1(cls, intervals):
        start_value_mapper = {}
        for index, interval in enumerate(intervals):
            start_value_mapper[interval[0]] = index

        start_values = sorted(list(start_value_mapper.keys()))
        result = []

        for interval in intervals:
            end = interval[1]
            start = cls._search(start_values, end)
            result.append(start_value_mapper.get(start, -1))
        return result

    @classmethod
    def _search(cls, nums, target):
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid

        if start == len(nums):
            return None
        return nums[start]


if __name__ == "__main__":
    #print(Solution._search([1, 2, 3, 5, 7, 8], 6))
    print(Solution().findRightInterval([[1,2]]))
    print(Solution().findRightInterval([[3,4],[2,3],[1,2]]))
    print(Solution().findRightInterval([[1,4],[2,3],[3,4]]))
    print(Solution().findRightInterval)
