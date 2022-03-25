'''
题目描述：
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
'''
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        动态规划：
        要走到f[i][j]，只能从f[i-1][j]或f[i-1][j-1]走，选择其中路径最小的进行走，状态转移方程为：f[i][j] = min(f[i-1][j], f[i-1][j-1]) + triangle[i][j]

        第i行有i+1个元素，j的范围为[0,i]，i和j都是从0开始的
        j=0,即在三角形最左侧时，f[i][0] = f[i-1][0] + triangle[i][0]
        j=i,即在三角形最右侧时，f[i][i] = f[i-1][i-1] + triangle[i][i]
        最终的答案为f[n-1][0]到f[n-1][n-1]的最小值
        '''
        # 三角形的深度
        n = len(triangle)
        # 初始化一个同样的三角形
        f = [[0] * n for _ in range(n)]
        # 初始化第一行 
        f[0][0] = triangle[0][0]
        
        for i in range(1,n):
            # j=0,即在三角形最左侧时，f[i][0] = f[i-1][0] + triangle[i][0]
            f[i][0] = f[i-1][0] + triangle[i][0]
            for j in range(1,i):
                f[i][j] = min(f[i-1][j-1],f[i-1][j]) + triangle[i][j]
            # j=i,即在三角形最右侧时，f[i][i] = f[i-1][i-1] + triangle[i][i]
            f[i][i] = f[i-1][i-1] + triangle[i][i]
        return min(f[n-1])

if __name__ == '__main__':
    # triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]   # 11
    triangle = [[5],[4,7],[8,9,10],[3,2,1,6]]
    s = Solution()
    print(s.minimumTotal(triangle))
    pass
