'''你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。

 实例1：
 输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。

'''
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
import math
global bad

def isBadVersion(target):
     if target == bad:
         return True
     else:
         return False

class Solution:
    def firstBadVersion(self, n):
         """
         :type n: int
         :rtype: int
         """
         l = 1
         r = n
         while l <= r:
             mid = int(l + (r - l) / 2)   # 这样计算是为了防止溢出
             if isBadVersion(mid):   # 是坏的版本，则第一次坏的在左边区间
                 r = mid - 1
             else:    # 不是坏的版本，则第一次坏的在右边区间
                 l = mid + 1
         return l

if __name__:
    versions = []
    n = int(input("输入版本的长度：\n"))
    # for i in range(n):
        # tmp = int(input("数组的内容\n"))
    bad = int(input("坏的版本数：\n"))
    s = Solution()
    result = s.firstBadVersion(n)
    print(result)
