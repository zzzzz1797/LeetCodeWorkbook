"""
    给你两个字符串s1和s2 ，写一个函数来判断 s2 是否包含 s1的排列。如果是，返回 true ；否则，返回 false 。
    换句话说，s1 的排列之一是 s2 的 子串 。


示例 1：
    输入：s1 = "ab" s2 = "eidbaooo"
    输出：true
    解释：s2 包含 s1 的排列之一 ("ba").

示例 2：
    输入：s1= "ab" s2 = "eidboaoo"
    输出：false

提示：
    1 <= s1.length, s2.length <= 104
    s1 和 s2 仅包含小写字母
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pass

    @classmethod
    def solve_1(cls, s1: str, s2: str):
        s1_length = len(s1)
        s2_length = len(s2)

        # 特殊情况处理
        if s1_length > s2_length:
            return False

        # 对字符串进行 获取对应字母以及出现的频次
        hash_map = {}
        for s_char in s1:
            hash_map[s_char] = hash_map.get(s_char, 0) + 1

        left = 0

        for right in range(s2_length):
            right_char = s2[right]

            hash_map[right_char] = hash_map.get(right_char, 0) - 1

            while hash_map[right_char] < 0:
                left_char = s2[left]
                hash_map[left_char] = hash_map.get(left_char, 0) + 1
                left += 1
            if right - left + 1 == s1_length:
                return True
        return False


if __name__ == "__main__":
    print(Solution.solve_1("ab", "123"))
