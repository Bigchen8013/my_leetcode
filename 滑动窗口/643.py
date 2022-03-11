'''
给你一个由 n 个元素组成的整数数组 nums 和一个整数 k 。

请你找出平均数最大且 长度为 k 的连续子数组，并输出该最大平均数。

任何误差小于 10-5 的答案都将被视为正确答案。

输入:nums = [1,12,-5,-6,50,3], k = 4
输出:12.75
解释:最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
'''

from typing import List
import math

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # step1：定义维护的变量
        sum, max_average = 0, -math.inf

        # step2：定义首位端口
        start = 0
        for end in range(len(nums)):
            # step3: 更新需要维护的变量  
            sum += nums[end]
            if end - start + 1 == k:
                max_average = max(max_average, sum / k)

            # step4: 更新窗口同时更新维护的变量
            if end >= k-1:
                sum -= nums[start]
                start += 1
        # step5： 返回最后的结果
        return max_average

if __name__ == '__main__':
    nums = [1,12,-5,-6,50,3]
    k = 4
    solution = Solution()
    result = solution.findMaxAverage(nums, k)
    print(result)