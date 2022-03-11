'''
题目描述：
有一个书店老板，他的书店开了 n 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 n 的整数数组 customers ，其中 customers[i] 是在第 i 分钟开始时进入商店的顾客的编号，所有这些顾客在第 i 分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 i 分钟生气，那么 grumpy[i] = 1，否则 grumpy[i] = 0。

当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 minutes 分钟不生气，但却只能使用一次。

请你返回 这一天营业下来，最多有多少客户能够感到满意 。
'''

from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
         # 满意的总数
         num_ = 0

         # 计算总的满意顾客有多少
         for i in range(len(grumpy)):
             if grumpy[i] == 0:
                 num_ += customers[i]
         
         # 生气时的顾客数和发动技能时的
         sum_ , max_sum_ , max_start = 0, 0, 0 
         
         start = 0 
         for end in range(len(grumpy)):
             if grumpy[end] == 1:
                 sum_ += customers[end]
             if sum_ > max_sum_:
                 max_sum_ = sum_
                 max_start = start

             if end >= minutes - 1:
                 if grumpy[start]:
                     sum_ -= customers[start]
                 start += 1
         # 老板成功抑制怒火的时间段为max_start---max_start + minutes
         # 记录老板生气时的顾客数
         g_nums = 0
         for i in range(max_start, max_start + minutes):
             if grumpy[i]:
                 g_nums += customers[i]
         
         return num_ + g_nums

if __name__:
    # customers = [1,0,1,2,1,1,7,5]
    # grumpy = [0,1,0,1,0,1,0,1]
    # minutes = 3
    # 16

    customers = [1]
    grumpy = [0]
    minutes = 1

    s = Solution()
    result = s.maxSatisfied(customers, grumpy, minutes)
    print(result)
