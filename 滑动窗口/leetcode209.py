'''
给定一个含有n个正整数的数组和一个正整数 target 。

找出该数组中满足其和sum ≥ target 的长度最小的 
连续子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

'''
from typing import List
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
         sum_, min_len = 0, len(nums)+1
         start = 0
         g_sum = 0 
         for end in range(len(nums)):
             sum_ += nums[end]
             
             while sum_ >= target:
                 g_sum = sum_
                 min_len = min(min_len, end - start +1)
                 sum_ -= nums[start]
                 start += 1
        
         if g_sum == 0:
             return 0
         return min_len



if __name__ == "__main__":
    nums = [12,28,83,4,25,26,25,2,25,25,25,12]
    target = 213

    solution = Solution()

    result = solution.minSubArrayLen(target, nums)
    print(result)
