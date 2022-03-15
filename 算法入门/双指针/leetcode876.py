'''
题目描述;
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

示例1：
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.


示例2：
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

'''

from six.moves import xrange
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 单指针，一个指针遍历一遍求出链表的长度，另一个指针从头遍历到中间返回元素值
    def middleNode(self, head: ListNode) -> ListNode:
        start, end = head, head
        l_list = 0
        mid = 0
        while end :
            end = end.next
            l_list += 1
        
        while mid < l_list // 2:
            mid += 1
            start = start.next
        return start

    # 使用数组来存储并通过下标访问
    def middleNode1(self, head: ListNode) -> ListNode:
        result = []
        point = head
        while point:
            result.append(point)
            point = point.next
        return result[len(result)//2]
    # 快慢指针法，一个指针一次走一步，一个指针一次走两步，当快指针到达末尾时，慢指针在中间位置
    def middleNode2(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
