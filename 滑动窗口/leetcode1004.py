'''
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。

返回仅包含 1 的最长（连续）子数组的长度。

示例1:
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释： 
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。


'''

from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
         hashmap = {}
         max_len = 0
         start = 0

         for end in range(len(nums)):
             tail = nums[end]
             hashmap[tail] = hashmap.get(tail,0) + 1
             
             if hashmap.get(0,0) == k:
                 max_len = max(max_len, end - start + 1)
             
             while hashmap.get(0,0) > k:
                 head = nums[start]
                 hashmap[head] -= 1

                 start += 1
         return max_len

if __name__ == "__main__":
    solution = Solution()

    # nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
    # k = 3

    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    result = solution.longestOnes(nums, k)

    print(result)