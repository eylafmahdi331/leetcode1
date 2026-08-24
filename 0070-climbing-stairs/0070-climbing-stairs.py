class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        dp = {
        1: 1,
        2: 2,
        3: 3
        }
        if n <= 3:
                return n 
        else:
            for i in range(4, n + 1):
            

                dp[i] = dp[i-1] + dp[i - 2]
        last_value = list(dp.values())[-1]
        return last_value

        