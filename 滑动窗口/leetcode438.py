'''
给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

'''
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
         # 存储对比子串的哈希表  
         hashmap_p = {}
         for ch in p :
             hashmap_p[ch] = hashmap_p.get(ch,0) + 1
         
         llp = len(hashmap_p)
         # 存储子串的起始索引
         res = []

         start = 0
         # 存储s中的字串哈希表   
         hashmap = {}

         for end in range(len(s)):
             tail = s[end]
             hashmap[tail] = hashmap.get(tail,0) + 1
             # 两个哈希表相同则为异位词，添加开始索引 
             if hashmap == hashmap_p:
                 res.append(start)
             # 当前子串的长度大于设定的，则说明需要更新hashmap的内容
             if end >= llp-1: 
                 head = s[start]
                 hashmap[head] -= 1
                 if hashmap[head] == 0:
                     del hashmap[head]
                 start += 1
         return res

                 
if __name__ == "__main__":
    solution = Solution()

    s = "cbaebabacd"
    p = "abc"

    result = solution.findAnagrams(s, p)
    print(result)