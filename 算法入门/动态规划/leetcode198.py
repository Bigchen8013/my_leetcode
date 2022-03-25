'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
'''

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        动态规划
        第一间房：S1=H1=1
        第二间房：S2=max(S1,H2)，第一间与第二间谁大，就抢谁的钱
        第三间房：S3=max(S2,S1+H3)，偷第一间和第三间与偷第二间的钱比较，哪种最大就偷哪种
        第四间房：S4=max(S3,S2+H4)，若是偷第四间，则可以偷第二间，然后与前三间房的方案比较
        ...
        递推公式：S[i]=max(S[i-1],S[i-2]+nums[i])

        '''
        n = len(nums)
        if n == 0:
            return 0
        # 如果只有一个房间，那么只能偷第一个房间
        if n == 1:
            return nums[0]
        
        # 初始化一个状态数组，用于存储每个房间的最大值
        state = [0] * n 
        state[0] = nums[0]
        state[1] = max(nums[0], nums[1])
        for i in range(2, n):
            state[i] = max(state[i-1], state[i-2] + nums[i])
        return state[n-1]

    def rob1(self, nums: List[int]) -> int:
        '''
        动态规划，滚动数组，优化空间复杂度为1
        '''
        n = len(nums)
        if n == 0:
            return 0
        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, n):
            third = max(second, first + nums[i])
            first = second
            second = third
        return second



if __name__:
    s = Solution()
    nums = [2,7,9,3,1]
    print(s.rob(nums))
    print(s.rob1(nums))
