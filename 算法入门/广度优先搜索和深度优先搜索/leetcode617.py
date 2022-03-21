'''

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        '''
        将两棵树的值都合并到第一颗树中，最后返回树1
        '''
        def DFS(tree1,tree2):
            # tree1和tree2中，只要有一个是null，函数直接返回
            if not (tree1 and tree2):
                return tree1 if tree1 else tree2
            # tree1的值等于两棵树之和
            # 递归遍历并计算两棵树的左右子树
            tree1.val += tree2.val
            tree1.left = DFS(tree1.left, tree2.left)
            tree1.right = DFS(tree1.right, tree2.right)
            return tree1
        
        return DFS(root1, root2)
