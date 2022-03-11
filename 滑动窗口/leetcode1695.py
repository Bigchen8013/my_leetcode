'''
给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是a 的一个子数组。

'''

from typing import List
import math

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
         # Step 1
         # 定义需要维护的变量, 本题最大得分，所以需要定义当前得分sum_和最大得分max_sum
         # 本题又涉及去重 (题目规定子数组不能有重复)，因此还需要一个哈希表

         sum_, currentsum, hashmap = 0, 0, {}
         start = 0 
    
         for end in range(len(nums)):
             # Step 3
             # 更新需要维护的变量 (sum_, hashmap)
             # sum和hashmap需要更新就不说了，max_sum当且仅当哈希表里面没有重复元素时 (end - start + 1 == len(hashmap)) 更新
             tmp = nums[end]
             sum_ += tmp
             hashmap[tmp] = hashmap.get(tmp,0) + 1

             if end - start + 1 == len(hashmap):
                 currentsum = max(currentsum,sum_)
             # Step 4
             # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
             # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
             # 哈希表里面有重复元素时 (end - start + 1 > len(hashmap)) 窗口不合法
             # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap， sum_)

             while end -start + 1 > len(hashmap):
                 head = nums[start]
                 hashmap[head] -= 1

                 if hashmap[head] == 0:
                     del hashmap[head]

                 sum_ -= head
                 start += 1
         return currentsum

if __name__ == '__main__':

    solution = Solution()
    nums = [4,2,4,5,6]
    result = solution.maximumUniqueSubarray(nums)
    print(result)
