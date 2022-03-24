'''
题目描述：
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
'''
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def DFS(cur, n, tmp):
            # tmp的长度加上剩余的长度小于指定的长度k，直接返回
            if len(tmp) + n - cur + 1 < k:
                return 
            # 记录满足的长度的答案
            if len(tmp) == k:
                result.append(tmp)
                return
            # 考虑选择当前位置
            DFS(cur + 1, n, tmp+[cur])
            # 考虑不选择当前位置
            DFS(cur + 1, n, tmp)
        
        DFS(1, n, [])
        return result

if __name__:
    s = Solution()
    n = 4
    k = 2

    result = s.combine(n, k)
    print(result)