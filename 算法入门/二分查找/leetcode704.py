'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
'''
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
         start = 0
         end = len(nums) -1 
        
         while start <= end:
             mid = int((start + end) / 2)
             if nums[mid] == target:
                 return mid
             elif nums[mid] < target:
                 start = mid + 1
             else:
                 end = mid - 1
         return -1

if __name__:
    # nums = [-1,0,3,5,9,12]
    # target = int(input("输入target的数：\n"))
    # len_num = int(input("输入nums 的长度：\n"))
    # nums = []
    # for i in range(len_num):
    #     tmp = int(input("nums的内容：\n"))
    #     nums.append(tmp)

    nums = [-1,0,3,5,9,12]
    target = 2
    s = Solution()
    result = s.search(nums, target)
    print(result)
