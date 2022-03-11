'''
题目描述：
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。
'''

from typing import List
import math
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
         # 找出非首尾串的最小连续字串
         sum_, min_sum = 0, math.inf

         n = len(cardPoints)
         # 特解
         if k == n:
             return sum(cardPoints)
         # 非首尾串的最大长度，可用于控制滑动窗口的大小
         m = n - k

         start = 0
         for end in range(n):
             sum_ += cardPoints[end]

             if end >= m - 1:
                 min_sum = min(sum_, min_sum)
                 sum_ -= cardPoints[start]
                 start += 1
         return sum(cardPoints) - min_sum

if __name__:
    # cardPoints = [1,2,3,4,5,6,1]
    # k = 3
    # 12
    # cardPoints = [1,50,30,40,0,15,10]
    # k = 3
    # 81
    l_c = input("输入cardPonits长度：\n")
    l_c = int(l_c)
    cardPoints = []
    for i in range(l_c):
        tmp = input("数组的内容:\n")
        tmp = int(tmp)
        cardPoints.append(tmp)
    k = input("首尾子串的长度\n")
    k = int(k)
    s = Solution()
    result = s.maxScore(cardPoints, k)
    print(result)


