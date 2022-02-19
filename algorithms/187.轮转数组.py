"""
给你一个数组，将数组中的元素向右轮转 k个位置，其中k是非负数。

示例 1:
    输入: nums = [1,2,3,4,5,6,7], k = 3
    输出: [5,6,7,1,2,3,4]
    解释:
    向右轮转 1 步: [7,1,2,3,4,5,6]
    向右轮转 2 步: [6,7,1,2,3,4,5]
    向右轮转 3 步: [5,6,7,1,2,3,4]

示例2:
    输入：nums = [-1,-100,3,99], k = 2
    输出：[3,99,-1,-100]
    解释:
    向右轮转 1 步: [99,-1,-100,3]
    向右轮转 2 步: [3,99,-1,-100]

提示：
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

进阶：
    尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
    你可以使用空间复杂度为O(1) 的原地算法解决这个问题吗？

"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pass

    @classmethod
    def solve_1(cls, nums, k):
        length = len(nums)

        k = k % length

        cls.reverse(nums, 0, length - 1)
        cls.reverse(nums, 0, k - 1)
        cls.reverse(nums, k, length - 1)

    @classmethod
    def reverse(cls, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
