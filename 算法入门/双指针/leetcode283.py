'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''

from typing import List
from six.moves import xrange

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # 两个指针i和j，i指针总是去找非0的位置来与j指针进行交换，保证了非0的元素相对位置不变
        j = 0
        for i in xrange(len(nums)):
            if nums[i]:   # i指针找到非0的元素，将其与j指针进行交换
                print(nums[i],nums[j])
                nums[j],nums[i] = nums[i],nums[j]
                j += 1
        print(nums)     
        pass


    def moveZeroes1(self, nums: List[int]) -> None:
        '''
        空间复杂度为O(len(nums)),创建一个新列表，遍历nums，当为0时，尾部添加到新列表，部位0时，从头部开始添加
        '''
        tmp = []
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp.append(nums[i])
            else:
                tmp.insert(j, nums[i])
                j += 1
        
        print(tmp)
    
    def moveZeroes2(self, nums: List[int]) -> None:
        '''
        遍历nums，遇到元素为0，则将其pop出来，然后append到末尾
        '''
        if not nums:
            return 0
        ll = len(nums)
        if ll == 1:
            print(nums)
            return
        
        p = 0
        while True:
            if nums[p] == 0:
                nums.pop(p)
                nums.append(0)
                ll -= 1
            else:
                p += 1
            if p == ll:
                print(nums)
                return
        



if __name__:

    # nums = [0,1,0,3,12]
    nums = [1,0]
    s = Solution()
    # s.moveZeroes1(nums)
    # s.moveZeroes(nums)
    s.moveZeroes2(nums)