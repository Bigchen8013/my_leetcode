'''
题目描述：
给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
'''
from typing import List
from six.moves import xrange
class Solution:
    def reverseWords(self, s: str) -> str:
        ls = s.split(" ")
        result = []
        for word in ls:
            result.append(word[::-1])
        return " ".join(result)
                
if __name__:
    solution = Solution()
    s = "Let's take LeetCode contest"
    result = solution.reverseWords(s)
    print(result)
