'''
给你两个长度相同的字符串，s 和 t。

将 s中的第i个字符变到t中的第 i 个字符需要|s[i] - t[i]的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

'''
import math
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
         currentCost = 0
         max_len = 0

         start = 0
         for end in range(len(t)):
             currentCost += abs(ord(t[end]) - ord(s[end]))
             if currentCost <= maxCost:
                 max_len = max(max_len, end - start +1)
             
             while currentCost > maxCost:
                 
                 currentCost -= abs(ord(t[start]) - ord(s[start]))
                 start += 1
         return max_len

if __name__ == "__main__":
    solution = Solution()
    s = "abcd"
    t = "bcdf" 
    maxCost = 3

    result = solution.equalSubstring(s, t, maxCost)
    print(result)