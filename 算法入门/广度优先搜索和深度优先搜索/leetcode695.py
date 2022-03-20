'''
题目描述：
给你一个大小为 m x n 的二进制矩阵 grid 。

岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在 水平或者竖直的四个方向上 相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。

岛屿的面积是岛上值为 1 的单元格的数目。

计算并返回 grid 中最大的岛屿面积。如果没有岛屿，则返回面积为 0 。

 
'''
from typing import List
from six.moves import xrange
from queue import Queue
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def DFS(x, y):
            cur_sum = 0   # 记录岛屿的面积
            # 递归的边界, 就是if里取非
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                cur_sum += 1
                grid[x][y] = 0   # 设置为0，就不会有重复计算
                # 分别从四个方向上进行遍历
                cur_sum += DFS(x + 1, y)
                cur_sum += DFS(x - 1, y)
                cur_sum += DFS(x, y + 1)
                cur_sum += DFS(x, y - 1)

            return cur_sum
        
        res = []    # 记录每块陆地的面积
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:   # 当遇到岛屿时进行深度优先遍历
                    sum_ = DFS(i, j)
                    res.append(sum_)

        if not res:  # 没有陆地的情况
            return 0
        else:
            print(res)  # 所有的岛屿面积
            return max(res)   # 返回最大值
    
    # 使用广度优先遍历来实现
    def maxAreaOfIsland1(self, grid: List[List[int]]) -> int:
        def BFS(x,y):
            que = Queue()  # 初始化一个队列
            cur_sum = 0
            que.put((x,y))  # 第一个点加入队列中

            while not que.empty():
                x1, y1 = que.get()
                # 判断是否满足边界
                if 0 <= x1 < len(grid) and 0 <= y1 < len(grid[0]) and grid[x1][y1]:
                    grid[x1][y1] = 0   # 访问过，设置为1
                    cur_sum += 1  # 陆地面积加1
                    que.put((x1 - 1, y1)) # 将四周的加入到队列中
                    que.put((x1 + 1, y1))
                    que.put((x1, y1 - 1))
                    que.put((x1, y1 + 1))
            return cur_sum
        
        res = []
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == 1:
                    tmp = BFS(i,j)
                    res.append(tmp)
        
        if not res:
            return 0
        print("1:",res)
        return max(res)



if __name__:
    s = Solution()
    s1 = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    # [1, 4, 4, 5, 6, 5]
    # grid = [[0,0,0,0,0,0,0,0]]
    result = s.maxAreaOfIsland(grid)
    print("result:",result)
    # 此处运行时result1始终为0，原因是方法一将1的地方设置为0了
    result1 = s1.maxAreaOfIsland1(grid)
    print("result1:",result1)
