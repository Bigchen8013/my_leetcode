'''
给你一个下标从 1 开始的整数数组 numbers ，该数组已按 非递减顺序排列  ，请你从数组中找出满足相加之和等于目标数 target 的两个数。如果设这两个数分别是 numbers[index1] 和 numbers[index2] ，则 1 <= index1 < index2 <= numbers.length 。

以长度为 2 的整数数组 [index1, index2] 的形式返回这两个整数的下标 index1 和 index2。

你可以假设每个输入 只对应唯一的答案 ，而且你 不可以 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。

'''
from typing import List
from six.moves import xrange
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        双指针，从左和右分别开始查找
        '''
        ll = len(numbers) # 列表的长度
        start = 0
        end = ll - 1
        result = []
        while start < end:
            sum_ = numbers[start] + numbers[end]
            if sum_ < target:   # 小于目标值，左指针向右移动
                start += 1
            elif sum_ > target:   # 大于目标值，右指针向左移动
                end -= 1
            else:   # 等于的情况
                result.append(start+1)
                result.append(end+1)
                return result

        return [-1,-1]   # 暂时不清楚为什么是-1，-1
    # --------------------------------------------------------------------------
    # 使用二分法求解：有序数组，固定一个数，使用二分法查找另一个数
    def binatySearch(self,numbers: List[int], target: int, left:int) -> int:
        l = left
        r = len(numbers) - 1

        while l <= r:
            mid = int(l + (r - l) / 2)
            if numbers[mid] > target:
                r = mid - 1
            elif numbers[mid] < target:
                l = mid + 1
            else:
                return mid   # 找到返回下标
        return -1    # 未找到返回-1

    def twoSum1(self, numbers: List[int], target: int) -> List[int]:
        result = []
        # if numbers[0] > target:    # 最小的数都大于目标，返回空,有负数时这个情况就不成立
        #     return result
        for i in xrange(len(numbers)):
            tmp = target - numbers[i]
            isSearch = self.binatySearch(numbers, tmp, i + 1)   # i+1是直接从固定数的右边开始使用二分法查找
            # print(isSearch)
            if isSearch != -1:
                result.append(i + 1)
                result.append(isSearch + 1)
        return result

if __name__:
    numbers = [-1,-1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = -2

    s = Solution()
    result = s.twoSum(numbers, target)
    print(result)
    result1 = s.twoSum1(numbers, target)
    print(result1)

    # result = s.binatySearch(numbers, target)
    # print(result)