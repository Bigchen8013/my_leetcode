'''
题目描述：
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''

from six.moves import xrange
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # 双指针方法，首先两个指针都指向头，倒数n个节点，那么快指针第一次就先走n步，然后快慢指针每次一步一步走，当快指针到达尾部时，慢指针所指的位置就是要删除的位置
    # 添加一个哑指针，作为head的前前驱，这样不需要对头结点进行特殊的判断
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0,head)   # 哑指针
        fast = slow = dummy

        for i in xrange(n + 1):   # 相当于往后先退了一步，所有走的时候多走一步
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
    # 先遍历链表，得到长度，然后再走length-n+1步，进行操作
    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        length = 0
        dummy = ListNode(0,head)
        point = dummy
        while head:
            length += 1
            head = head.next
        for i in xrange(length - n ): # 本来应该是length -n +1 的，由于先退了一步，所以就往前走length -1步
            point = point.next
        point.next = point.next.next

        return dummy.next