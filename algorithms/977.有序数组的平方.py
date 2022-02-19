"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
    输入：nums = [-4,-1,0,3,10]
    输出：[0,1,9,16,100]
    解释：平方后，数组变为 [16,1,0,9,100]
    排序后，数组变为 [0,1,9,16,100]

示例 2：
    输入：nums = [-7,-3,2,3,11]
    输出：[4,9,9,49,121]

提示：
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums 已按 非递减顺序 排序

进阶：
    请你设计时间复杂度为 O(n) 的算法解决本问题
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pass

    @classmethod
    def solve_1(cls, nums):
        length = len(nums)

        left = 0
        right = length - 1

        res = [-1] * length
        site = length - 1

        while left <= right:
            left_value = nums[left] * nums[left]
            right_value = nums[right] * nums[right]

            if left_value > right_value:
                res[site] = left_value
                left += 1
            else:
                res[site] = right_value
                right -= 1

            site -= 1

        return res


if __name__ == "__main__":
    print(Solution.solve_1([-4, -1, 0, 3, 10]))
