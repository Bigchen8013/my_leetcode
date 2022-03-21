'''
题目描述：
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。
函数应该填充它的每个 next 指针，以指向其下一个右侧节点，。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from queue import Queue
from six.moves import xrange
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        方法一，使用层次遍历的方法实现
        '''
        # 将每一层的元素都放入队列中，然后遍历队列中的元素，将左边节点的next指针指向右边的节点
        if not root:    # 为空则返回
            return root
        que = [root]
        # 将根节点加入队列中

        # 每一层进行遍历
        while not que.empty():
            cur_size = len(que)  # 记录当层的元素个数
            for i in xrange(1,cur_size):
                # 从队首取出元素
                node = que.pop(0)
                if i < cur_size:
                    node.next = que[0]
                # 拓展节点
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return root
    
    def connect1(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ''' 方法二：利用next指针来进行
        通过父节点可以连接两个孩子节点：node.left.next = node.right
        由于在N层时，N+1层的next指针已经建立好，可以通过同一层的node.next找到相邻的父节点：node.right.next = node.next.left
        最左边的节点当做头结点，同一层的相当于单链表的遍历
        当root.left为NULL的时候，整棵树都遍历完成
        '''
        if not root:
            return root
        
        leftnode = root

        while leftnode.left:
            head = leftnode
            while head:
                # 为下一层建立节点联系
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            # 遍历下一层
            leftnode = leftnode.left
        return root
        