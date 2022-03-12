
'''
题目描述：
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。
'''

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

         l = 0
         r = len(nums) - 1
         # 特解
         if target < nums[l]:    # 小于最小的，返回0
             return 0
         if target > nums[r]:    # 大于最大的，返回r+1
             return r + 1  
         
         while l <= r:
             mid = int(l + (r -l) / 2)   # 防止溢出，等同于（l + r ）/2
             if target > nums[mid]:
                 l = mid + 1
             elif target < nums[mid]:
                 r = mid -1
             else:
                 return mid
         return r + 1

if __name__:
    # num_l = int(input("输入数组的长度\n"))
    nums = [1,3,5,6]
    target = 5
    s = Solution()
    result = s.searchInsert(nums, target)
    print(result)
    