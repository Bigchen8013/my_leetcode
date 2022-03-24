'''
题目要求：
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
from six.moves import xrange
class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        一次可以爬1级或2级，则第n级台阶的方法数=n-1级台阶的方法数+n-2级台阶的方法数

        fn = f(n-1)+f(n-2)
        递归的方法
        n =44的时候超出时间限制
        '''
        if 1 <= n <= 2:
            return n
        
        return self.climbStairs(n -1) + self.climbStairs(n - 2)

    def climbStairs1(self, n: int) -> int:
        # 用于存储计算过的值，避免重复计算
        memo = [0 for _ in xrange(n + 1)]

        def climbStairs1Memo(n, memo):
            if memo[n] > 0:
                return memo[n]
            if n == 1:
                memo[n] = 1
            elif n == 2:
                memo[n] = 2
            else:
                num1 = climbStairs1Memo(n - 1, memo)
                num2 = climbStairs1Memo(n - 2, memo)
                memo[n] = num1 + num2
            return memo[n]

        return climbStairs1Memo(n, memo)

    # 动态规划的方法
    def climbStairs2(self, n: int) -> int:
        '''
        动态规划的方法,
        还可以使用斐波那契数列的方式将动态规划的方法空间复杂度优化到1
        '''
        # 斐波那契数列的方法------
        # if n == 1:
        #     return 1
        # first = 1
        # second = 2

        # for i in xrange(3, n+1):
        #     third = first + second
        #     first = second
        #     second = third
        
        # return second
        # -----------------------
        if n == 1:
            return 1
        dp = [0 for _ in xrange(n + 1)]
        dp[1] = 1
        dp[2] = 2

        for i in xrange(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        
        return dp[n]



if __name__:

    s = Solution()
    # n = 2   # 2

    n = 3

    result = s.climbStairs2(n)
    print("递归的方法：",result)