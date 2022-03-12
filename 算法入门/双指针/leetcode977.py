'''
题目描述：
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

'''

from typing import List
import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
         start = 0
         end = len(nums) - 1 
         result = []
         while start <= end:
             if abs(nums[start]) > abs(nums[end]):
                 tmp = nums[start] ** 2
                 result.insert(0, tmp)
                 start += 1
             else:
                 tmp = nums[end] ** 2
                 result.insert(0, tmp)
                 end -= 1
         return result

if __name__:
    # nums = [-4,-1,0,3,10]     # [0, 1, 9, 16, 100]
    nums = [-7,-3,2,3,11]    # [4, 9, 9, 49, 121]
    s = Solution()
    result = s.sortedSquares(nums)
    print(result)

    