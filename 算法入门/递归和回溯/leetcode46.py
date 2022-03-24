'''
题目描述：

给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
'''
from typing import List
from six.moves import xrange
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrace(first = 0):
            if first == n:
                result.append(nums[:])
            
            for i in xrange(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 递归下一个数
                backtrace(first + 1)
                # 撤销交换操作
                nums[first], nums[i] = nums[i], nums[first]
            
        n = len(nums)
        backtrace()
        return result
    
    # 以空间换时间的方式，设置状态变量实现
    def permute1(self, nums: List[int]) -> List[List[int]]:

        def DFS(nums, n, depth, path, used, res):
            '''
            nums: 表示的是数组
            n：数组的长度
            depth：遍历到第几层
            path：存储路径上值
            used：是否选择过该值
            res：存储结果
            '''
            if depth == n:
                res.append(path[:])
                return
            
            for i in xrange(n):
                # 如果当前值没有选择过，进行选择
                if not used[i]:
                    used[i] = 1
                    path.append(nums[i])
                    # 递归遍历
                    DFS(nums, n, depth + 1, path, used, res)
                    # 遍历结束后回溯
                    used[i] = 0
                    path.pop()
        n = len(nums)
        if n == 0:
            return []
        
        # 存储结果
        res = []
        # 设置访问数组，标记某数是否已经选择过，避免重复选择
        used = [0 for _ in xrange(n)]
        print(used)
        DFS(nums, n, 0, [], used, res)
        return res


if __name__:
    s = Solution()
    nums = [1,2,3]
    # result = s.permute(nums)
    result1 = s.permute1(nums)
    # print("result:",result)
    print("result1:",result1)
