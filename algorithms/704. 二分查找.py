"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

示例1：
    输入: nums = [-1,0,3,5,9,12], target = 9
    输出: 4
    解释: 9 出现在 nums 中并且下标为 4

示例2：
    输入: nums = [-1,0,3,5,9,12], target = 2
    输出: -1
    解释: 2 不存在 nums 中因此返回 -1

提示：
    1、你可以假设 nums 中的所有元素是不重复的。
    2、n 将在 [1, 10000]之间。
    3、nums 的每个元素都将在 [-9999, 9999]之间。

"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.solve_1(nums, target)

    @classmethod
    def solve_1(cls, nums, target):
        """
        基本的搜索方法，但是有一个缺陷：
        [1,2,2,2,3]， target=2,这种算法无法找到最左边的2 或者最右边的2
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            # 防止溢出的写法是 start + (end-start)//2
            mid = (start + end) // 2
            mid_value = nums[mid]
            if mid_value == target:
                return mid
            if mid_value > target:
                # 搜索区间是 [start, mid-1]
                end = mid - 1
            elif mid_value < target:
                # 搜索区间是 [mid+1, end]
                start = mid + 1
        return -1

    @classmethod
    def solve_2(cls, nums, target):
        """
        [1,2,2,2,3]， target=2  查找最左边的2
        检测空间是 [start, end)
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(nums)

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                start = mid + 1

        if start == len(nums) or nums[start] != target:
            return -1
        return start

    @classmethod
    def solve_3(cls, nums, target):
        """
        查找最右边的
        :param nums:
        :param target:
        :return:
        """
        start = 0
        end = len(target)

        while start < end:
            mid = (start + end) // 2

            if nums[mid] == target:
                start = mid + 1
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1

        if end < 0 or nums[end] != target:
            return -1
        return end
