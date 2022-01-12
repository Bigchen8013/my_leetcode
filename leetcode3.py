'''
给定一个字符串s，请你找出其中不含有重复字符的 最长子串 的长度。
示例1：
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

'''
# from typing import stdlib_re
import math

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        # step1: 定义维护变量，本题中定义的是最大的长度，以及哈希表
        max_len = -math.inf
        hashmap = {}

        # step2: 定义指针的开头和结尾
        start = 0
        for end in range(len(s)):
            # step3: 更新维护变量
            # 将窗口末端加入到哈希表并使其频率加1
            hashmap[s[end]] = hashmap.get(s[end],0) + 1

            if len(hashmap) == end -start + 1:
                max_len = max(max_len,len(hashmap))

            # step4: 
            # 根据题意,  题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 这时要用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 当窗口长度大于哈希表长度时候 (说明存在重复元素)，窗口不合法
            # 所以需要不断移动窗口左指针直到窗口再次合法, 同时提前更新需要维护的变量 (hashmap)
            while end - start + 1 > len(hashmap):
                head_item = s[start]
                hashmap[head_item] -= 1
                if hashmap[head_item] == 0:
                    del hashmap[head_item]
                start += 1
        return max_len

if __name__ == '__main__':
    # s = 'abcddsc'
    s = input("请输入一个字符串：\n")
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    print(result)
