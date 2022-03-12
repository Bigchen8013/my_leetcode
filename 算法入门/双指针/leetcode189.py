'''
题目描述：
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数
'''

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        切片的方法
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]
        print(nums)

    
    # 方法一：(len(nums) + k) % len(nums) = 当前下标
    # 使用的空间复杂度为O(len(nums))
    def rotate1(self, nums: List[int], k: int) -> None:
        result = []
        result.extend(nums)
        ll = len(nums)
        for i in range(len(nums)):
            tmp = (i + k) % ll 
            result[tmp] = nums[i]
        
        print(result)


if __name__:
    s= Solution()
    nums = [-1,-100,3,99]
    k = 2
    # nums = [1,2,3,4,5,6,7]
    # k = 3
    # s.rotate1(nums, k)
    s.rotate(nums, k)