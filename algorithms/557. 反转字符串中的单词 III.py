"""
    给定一个字符串s，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

示例 1：
    输入：s = "Let's take LeetCode contest"
    输出："s'teL ekat edoCteeL tsetnoc"

示例 2:
    输入： s = "God Ding"
    输出："doG gniD"

提示：

    1 <= s.length <= 5 * 104
    s包含可打印的 ASCII 字符。
    s不包含任何开头或结尾空格。
    s里 至少 有一个词。
    s中的所有单词都用一个空格隔开。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return self.solve_1(s)

    @classmethod
    def solve_0(cls, s: str) -> str:
        res = ""
        stack = []

        for i in s:
            if i != " ":
                stack.append(i)
            else:
                while stack:
                    res += stack.pop()
                res += " "

        while stack:
            res += stack.pop()

        return res

    @classmethod
    def solve_1(cls, s: str) -> str:
        res = ""

        start_index = last_index = 0
        length = len(s)

        while start_index < length:

            if s[start_index] == " ":
                res += cls._swap_word(s[last_index: start_index]) + " "

                while s[start_index] == " ":
                    start_index += 1
                last_index = start_index

            start_index += 1

        return res + cls._swap_word(s[last_index:start_index])

    @classmethod
    def _swap_word(cls, s):
        ans = ""
        right = len(s) - 1

        while right >= 0:
            ans += s[right]
            right -= 1
        return ans


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))
