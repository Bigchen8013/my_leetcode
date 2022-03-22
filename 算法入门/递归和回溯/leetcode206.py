'''
题目描述：


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        简单粗暴，遍历链表将值存入数组，然后再遍历一遍链表，将数组的值从尾部到头进行给链表赋值
        '''
        tmp_l = []
        # 遍历将值存入列表，然后使用翻转进行赋值
        point = head
        while point:
            tmp_l.append(point.val)
            point = point.next
        point = head
        while point:
            point.val = tmp_l.pop()
            point = point.next
        return head
    
        def reverseList1(self, head: ListNode) -> ListNode:
            '''
            迭代解法：
            设置两个指针pre和curr，每遇到一个节点就翻转next
            '''
            pre, curr = None, head
            
            while curr is not None:
                # 临时指针指向curr指针的next
                tmp = curr.next
                curr.next = pre
                pre = curr
                curr = tmp
            return pre
        
        def reverseList2(self, head: ListNode) -> ListNode:
            '''
            递归的解法：

            '''
            # 递归终止的条件，单链表为空或者单链表只有一个元素
            if not head or not head.next:
                return head
            
            # 递归的过程，不断将链表分为头结点和剩余节点的
            p = self.reverseList2(head.next)
            # 归的过程,将上一部分翻转后的节点与当前节点翻转
            head.next.next = head
            head.next = None

            return p
            