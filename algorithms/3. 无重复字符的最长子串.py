"""
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例1:
    输入: s = "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
    输入: s = "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
    输入: s = "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。 请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

提示：
    0 <= s.length <= 5 * 104
    s 由英文字母、数字、符号和空格组成
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

    @classmethod
    def solve_1(cls, s: str) -> int:
        """
        滑动窗口的做法
        :param s:
        :return:
        """
        max_len = 0
        exist_map = {}

        left = 0

        # 移动窗口有边界
        for right in range(len(s)):

            right_value = s[right]
            exist_map[right_value] = exist_map.get(right_value, 0) + 1

            if right - left + 1 == len(exist_map):
                # 说明窗口内没有重复的元素，并且尝试更新子串的长度
                max_len = max(max_len, right - left + 1)

            while right - left + 1 > len(exist_map):
                # 说明窗口内有重复的元素
                curr_value = s[left]

                # 移动左的窗口
                exist_map[curr_value] -= 1

                if exist_map[curr_value] == 0:
                    del exist_map[curr_value]
                left += 1
        return max_len


if __name__ == "__main__":
    print(Solution.solve_1("abcdbbe"))
