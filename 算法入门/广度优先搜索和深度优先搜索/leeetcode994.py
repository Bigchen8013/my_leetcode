'''
题目描述：
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
'''
from six.moves import xrange
from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        使用队列来解决
        先将腐烂的橘子位置加入到队列中，然后朝四个方向扩展，并将扩展后的加入到队列中（广度优先搜索）
        搜索结束检查还有没有为1的位置，若有则返回-1，没有则返回需要的分钟数
        '''
        m, n = len(grid), len(grid[0])
        # 存放坏橘子的位置
        bad_list = [(i,j) for i in xrange(m) for j in xrange(n) if grid[i][j] == 2]
        que = collections.deque(bad_list)
        new_bad_list = set(bad_list)
        count_s = 0   # 记录分钟数

        # 广度优先搜索
        while que:
            # 记录当前层的元素
            cur_size = len(que)
            # 遍历当前层的元素
            for z in xrange(cur_size):
                # 从队列中取出一个坏橘子的位置
                i, j = que.popleft()
                for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    # new_bad_list 防止重复
                    if 0 <= x < m and 0 <= y < n and (x,y) not in new_bad_list and grid[x][y] == 1:
                        grid[x][y] = 2
                        que.append((x,y))
                        new_bad_list.add((x,y))
            
            count_s += 1
        
        
        # 遍历一遍是否有新鲜橘子
        for i in xrange(m):
            for j in xrange(n):
                 if grid[i][j] == 1:
                     return -1
        if count_s == 0:
            return 0
        return count_s - 1
        
if __name__:
    s = Solution()
    # grid = [[2,1,1],[1,1,0],[0,1,1]]   # 4
    # grid = [[2,1,1],[0,1,1],[1,0,1]]    # -1
    # grid = [[0,2]]   # 0
    grid = [[0]]
    result = s.orangesRotting(grid)
    print(result)