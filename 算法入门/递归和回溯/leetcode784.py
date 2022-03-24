'''
题目描述：
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
'''

from typing import List
from six.moves import xrange
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''
        递归：
        从左到右遍历字符，rsult为已遍历过字符的字母大小写全排列
        例如，当 S = "abc" 时，考虑字母 "a", "b", "c"，初始令 ans = [""]，
        依次更新 ans = ["a", "A"]， ans = ["ab", "Ab", "aB", "AB"]， 
        ans = ["abc", "Abc", "aBc", "ABc", "abC", "AbC", "aBC", "ABC"]
        
        依次判断每个字符，若是字母，则将已经遍历过的字符串全排列复制一遍并在每个字符串的末尾加上小写（大写）的字符串
        遇到数字则直接添加到末尾
        '''
        result = [[]]

        for char in s:
            n = len(result)
            # 如果是字符串，则将result里的内容复制一遍，并将当前的字符串添加到末尾
            if char.isalpha():
                for i in xrange(n):
                    # 将当前已经遍历过的字符串复制一份
                    result.append(result[i][:])
                    # 添加小写的情况
                    result[i].extend(char.lower())
                    # 添加大写的情况
                    result[n + i].extend(char.upper())
            # 是数字的情况，直接加在每个字符串的末尾
            else:
                for i in xrange(n):
                    result[i].extend(char) 
        # 使用map函数将其中的内容进行拼接
        return list(map("".join, result))

    
    # 递归，深度优先遍历的方式
    def letterCasePermutation1(self, s: str) -> List[str]:
        '''
        递归
        深度优先搜索的策略
        '''

        digits = ['1','2','3','4','5','6','7','8','9','0']

        result = []

        def backtrace(ss, index):
            if index == len(s):
                result.append(ss)
                return None
            # 如果是数字。直接添加到末尾
            if s[index] in digits:
                backtrace(ss + s[index], index + 1)
                return None
            # 是字符的情况，大写添加一次递归，小写添加一次递归
            backtrace(ss + s[index].upper(), index + 1)
            backtrace(ss + s[index].lower(), index + 1)
            return None

        backtrace("", 0)
        return result


if  __name__:
    ss = Solution()
    s = "a1b2"
    result = ss.letterCasePermutation(s)
    print("result:",result)
    result1 = ss.letterCasePermutation1(s)
    print("result1:",result1)