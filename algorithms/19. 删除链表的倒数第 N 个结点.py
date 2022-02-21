"""
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
    输入：head = [1,2,3,4,5], n = 2
    输出：[1,2,3,5]

    5 - 2 =3

示例 2：
    输入：head = [1], n = 1
    输出：[]

示例 3：
    输入：head = [1,2], n = 1
    输出：[1]

    2- 1= 1


提示：
    链表中结点的数目为 sz
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def join(self, val):
        val = self.__class__(val)
        self.next = val
        return val

    def __str__(self):
        result = []
        curr = self
        while curr:
            result.append(curr.val)
            curr = curr.next
        return ",".join(map(str, result))


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        return self.solve_1(head, n)

    @classmethod
    def solve_1(cls, head, n):
        # 防止删除头节点
        dummy_node = ListNode(0)
        dummy_node.next = head

        fast_node = dummy_node
        slow_node = dummy_node

        while n + 1:
            fast_node = fast_node.next

            n -= 1

        while fast_node:
            fast_node = fast_node.next
            slow_node = slow_node.next

        slow_node.next = slow_node.next.next

        return dummy_node.next
