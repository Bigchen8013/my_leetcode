'''
题目描述;
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

解释：
https://leetcode-cn.com/problems/01-matrix/solution/2chong-bfs-xiang-jie-dp-bi-xu-miao-dong-by-sweetie/
 
'''
from six.moves import xrange
import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        使用广度优先搜索来解决问题，
        先把数组中0 的位置添加到队列中,找到所有距离为1的点，然后找距离为2的点，....

        '''
        m, n = len(mat), len(mat[0])
        # 初始化一个同样大小的数组，初始值为0
        dist = [[0] * n for _ in xrange(m)]
        # 将所有0的位置加入到列表中
        zeroes_pos = [(i,j) for i in xrange(m) for j in xrange(n) if mat[i][j] == 0]
        # 将列表加入到队列中
        q = collections.deque(zeroes_pos)
        seen = set(zeroes_pos)
        # 广度优先搜索
        while q:
            # 从队列左边出一个元素
            i, j = q.popleft()
            for x, y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0 <= x < m and 0 <= y < n and (x,y) not in seen:
                    dist[x][y] = dist[i][j] + 1
                    q.append((x,y))
                    seen.add((x,y))
        return dist